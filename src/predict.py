import cv2

from config import MODEL_PATH
from detector.yolo_detector import YOLODetector
from inspection import (
    ResultConverter,
    InspectionManager,
    DecisionEngine,
    InspectionReport,
    InspectionPipeline,
)
from visualizer import Visualizer


def main():

    image_path = "datasets\\test\\images\\l_light_01_missing_hole_18_1_600.jpg"

    image = cv2.imread(image_path)

    if image is None:
        print("Image not found.")
        return

    pipeline = InspectionPipeline(
        YOLODetector(MODEL_PATH),
        ResultConverter(),
        InspectionManager(),
        DecisionEngine(),
        InspectionReport(),
        Visualizer(),
    )

    report, output = pipeline.Process(image)

    print(report)

    cv2.imshow("Prediction", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()