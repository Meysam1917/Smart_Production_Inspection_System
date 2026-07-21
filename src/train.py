from ultralytics import YOLO


def main():
    model = YOLO("yolo11s.pt")

    model.train(
        data="datasets/data.yaml",
        imgsz=640,
        epochs=20,
        batch=16,
        device=0,
        project="runs",
        name="baseline_seg",
    )


if __name__ == "__main__":
    main()
