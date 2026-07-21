class DecisionEngine:
    DEFECT_PENALTIES = {
        "mouse_bite": 30,
        "open_circuit": 30,
        "missing_hole": 25,
        "short": 25,
        "spur": 10,
        "spurious_copper": 8,
    }

    def decide(self, defects):
        quality_score = 100

        for defect in defects:
            penalty = self.DEFECT_PENALTIES.get(defect.class_name, 0)
            quality_score -= penalty

        quality_score = max(0, quality_score)

        if quality_score >= 90:
            status = "PASS"
        elif quality_score >= 70:
            status = "REWORK"
        else:
            status = "REJECT"

        return {
            "quality_score": quality_score,
            "status": status,
            "total_defects": len(defects),
        }