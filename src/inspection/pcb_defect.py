class PCBDefect:
    def __init__(self, defect_id, class_name, confidence, bbox):
        self.id = defect_id
        self.class_name = class_name
        self.confidence = confidence
        self.bbox = bbox

    def __repr__(self):
        return (
            f"PCB_defect("
            f"id={self.id}, "
            f"class={self.class_name}, "
            f"confidence={self.confidence:.2f})"
        )