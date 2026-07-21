class InspectionManager:
    def __init__(self):
        self.defect = {}

    def clear(self):
        self.defect.clear()

    def generate(self, defects, inspection_result):
        report = {
            "quality_score": inspection_result["quality_score"],
            "status": inspection_result["status"],
            "total_defects": inspection_result["total_defects"],
            "defects": [],
        }

        for defect in defects:
            report["defects"].append(
                {
                    "id": defect.id,
                    "class": defect.class_name,
                    "confidence": defect.confidence,
                }
            )

        return report

    def add_defect(self, defect):
        self.defect[defect.id] = defect

    def add_defects(self, defects):
        for defect in defects:
            self.add_defect(defect)

    def remove_defect(self, defect_id):
        if defect_id in self.defect:
            del self.defect[defect_id]

    def get_defect(self, defect_id):
        return self.defect.get(defect_id)

    def get_all_defect(self):
        return list(self.defect.values())