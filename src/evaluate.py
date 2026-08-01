from ultralytics import YOLO

from config import MODEL_PATH


def main():

    model = YOLO("runs\\detect\\runs\\yolo26n\\weights\\best.pt")

    metrics = model.val()

    print("\nEvaluation Results")
    print("-" * 30)
    print(f"Precision : {metrics.box.mp:.4f}")
    print(f"Recall    : {metrics.box.mr:.4f}")
    print(f"mAP50     : {metrics.box.map50:.4f}")
    print(f"mAP50-95  : {metrics.box.map:.4f}")


if __name__ == "__main__":
    main()