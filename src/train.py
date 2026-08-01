from ultralytics import YOLO




def main():
    model = YOLO("yolo26m.pt")

    model.train(
        data="datasets/data.yaml",
        imgsz=640,
        epochs=11,
        batch=8,
        device=0,
        project="runs",
        name="test1",
        workers=8,
        # cache = "ram",
    )


if __name__ == "__main__":
    main()
