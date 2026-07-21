class InspectionReport:
    def generate(self, defects, decision):
        report = {
            "decision": decision,
            "total_defects": len(defects),
            "defects": [],
        }

        for defect in defects:
            report["defects"].append(
                {
                    "id": defect.id,
                    "class_name": defect.class_name,
                    "confidence": defect.confidence,
                    "bbox": defect.bbox,
                }
            )
        return report
