from config import MODEL_PATH, INPUT_FOLDER, OUTPUT_FOLDER
import json
from pathlib import Path
import cv2
from detector.yolo_detector import YOLODetector
from inspection import (
    DecisionEngine,
    InspectionManager,
    InspectionPipeline,
    InspectionReport,
    ResultConverter
)
from visualizer import Visualizer


test_folder = Path(INPUT_FOLDER)

pipeline = InspectionPipeline(
    YOLODetector(MODEL_PATH),
    ResultConverter(),
    InspectionManager(),
    DecisionEngine(),
    InspectionReport(),
    Visualizer(),
)

for image_path in test_folder.glob("*"):
    image = cv2.imread(str(image_path))
    if image is None:
        continue

    report, output = pipeline.Process(image)

    print(f"Processed {image_path.name}:")
    print("Inspection Report:", report)

    output_folder = Path(OUTPUT_FOLDER)
    output_folder.mkdir(exist_ok=True, parents=True)

    save_path = output_folder / image_path.name
    cv2.imwrite(str(save_path), output)

    report_path = output_folder / f"{image_path.stem}.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

cv2.imshow("Inspection Result", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("inspection_result.jpg", output)

with open("reports/report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4)
