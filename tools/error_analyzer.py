import cv2
from pathlib import Path
from ultralytics import YOLO

# ---- EDIT THESE PATHS ----
WEIGHTS_PATH = "runs\\yolo11\\weights\\best.pt"
IMAGES_DIR = "datasets/test/images"
LABELS_DIR = "datasets/test/labels"
OUTPUT_DIR = "wrong_detections_yolo1o"
RESULTS_FILE = "results-yolo11.txt"
IOU_THRESHOLD = 0.5
# ---------------------------

GREEN = (0, 200, 0)
RED = (0, 0, 255)
ORANGE = (0, 140, 255)


def load_labels(label_path, img_w, img_h):
    boxes = []
    if not Path(label_path).exists():
        return boxes
    with open(label_path) as f:
        for line in f:
            cls_id, xc, yc, w, h = map(float, line.split())
            xc, yc, w, h = xc * img_w, yc * img_h, w * img_w, h * img_h
            boxes.append([xc - w / 2, yc - h / 2, xc + w / 2, yc + h / 2, int(cls_id)])
    return boxes


def iou(box_a, box_b):
    x1 = max(box_a[0], box_b[0])
    y1 = max(box_a[1], box_b[1])
    x2 = min(box_a[2], box_b[2])
    y2 = min(box_a[3], box_b[3])

    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
    union = area_a + area_b - inter

    return inter / union if union > 0 else 0.0


def draw_box(img, box, color, label):
    x1, y1, x2, y2 = map(int, box[:4])
    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    cv2.putText(img, label, (x1, max(y1 - 8, 15)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


def main():
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    model = YOLO(WEIGHTS_PATH)
    image_paths = sorted(Path(IMAGES_DIR).glob("*.*"))

    log_lines = []
    total_tp, total_fp, total_fn = 0, 0, 0
    images_with_errors = 0

    for img_path in image_paths:
        result = model.predict(source=str(img_path), verbose=False)[0]
        img_h, img_w = result.orig_shape
        img = cv2.imread(str(img_path))

        gt_boxes = load_labels(Path(LABELS_DIR) / f"{img_path.stem}.txt", img_w, img_h)
        used_gt = set()
        has_error = False

        for box in result.boxes:
            pred_xyxy = box.xyxy[0].tolist()
            pred_cls = int(box.cls[0].item())
            conf = float(box.conf[0].item())

            best_iou, best_gt_idx = 0.0, -1
            for i, gt in enumerate(gt_boxes):
                if i in used_gt or gt[4] != pred_cls:
                    continue
                score = iou(pred_xyxy, gt)
                if score > best_iou:
                    best_iou, best_gt_idx = score, i

            if best_iou >= IOU_THRESHOLD:
                used_gt.add(best_gt_idx)
                total_tp += 1
                draw_box(img, pred_xyxy, GREEN, f"TP cls{pred_cls} {conf:.2f}")
            else:
                total_fp += 1
                has_error = True
                draw_box(img, pred_xyxy, RED, f"FP cls{pred_cls} {conf:.2f}")
                log_lines.append(f"{img_path.name}: FALSE POSITIVE  class={pred_cls}  "
                                  f"best_iou={best_iou:.2f}  conf={conf:.2f}")

        for i, gt in enumerate(gt_boxes):
            if i not in used_gt:
                total_fn += 1
                has_error = True
                draw_box(img, gt, ORANGE, f"MISSED cls{gt[4]}")
                log_lines.append(f"{img_path.name}: FALSE NEGATIVE (missed)  class={gt[4]}")

        if has_error:
            images_with_errors += 1
            out_path = Path(OUTPUT_DIR) / img_path.name
            cv2.imwrite(str(out_path), img)

    summary = [
        f"=== Detection Error Summary (IoU threshold = {IOU_THRESHOLD}) ===",
        f"Total images checked: {len(image_paths)}",
        f"Images with at least one error: {images_with_errors}",
        f"True Positives:  {total_tp}",
        f"False Positives: {total_fp}  (wrong/extra detections)",
        f"False Negatives: {total_fn}  (missed real defects)",
        "",
        "=== Per-error detail ===",
    ] + log_lines

    Path(RESULTS_FILE).write_text("\n".join(summary), encoding="utf-8")

    print("\n".join(summary[:6]))
    print(f"\nAnnotated error images saved to: {OUTPUT_DIR}/")
    print(f"Full results written to: {RESULTS_FILE}")


if __name__ == "__main__":
    main()