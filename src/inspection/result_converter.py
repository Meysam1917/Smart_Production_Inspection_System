from .pcb_defect import PCBDefect

class ResultConverter:
    def __init__(self):
        pass

    def convert(self, results):
        defects = []
        for result in results:
            boxes = result.boxes
            names = result.names

            if len(boxes) == 0:
                continue

            for box in boxes:
                class_id = int(box.cls[0])
                class_name = names[class_id]
                confidence = float(box.conf[0])
                bbox = box.xyxy[0].tolist()

                defect_id = len(defects) + 1
                defect = PCBDefect(
                    defect_id=defect_id,
                    class_name=class_name,
                    confidence=confidence,
                    bbox=bbox,
                )
                defects.append(defect)

        return defects
