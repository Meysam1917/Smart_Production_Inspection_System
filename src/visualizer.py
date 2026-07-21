import cv2
import numpy as np


class Visualizer:
    def draw(self, image, defects, inspection_result):
        if isinstance(image, str):
            image = cv2.imread(image)

        if image is None:
            raise FileNotFoundError(
                "Could not load image. Check if the file path is correct.")

        for defect in defects:
            x1, y1, x2, y2 = map(int, defect.bbox)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

            text = f"{defect.class_name} {defect.confidence:.2f}"
            cv2.putText(
                image,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
            )

        score = inspection_result["quality_score"]
        status = inspection_result["status"]

        cv2.putText(
            image,
            f"Quality: {score}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 0),
            2,
        )

        cv2.putText(
            image,
            f"Status: {status}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 0),
            2,
        )

        return image
