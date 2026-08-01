# Model Evaluation

## Evaluation Setup

All models were evaluated under identical conditions.

Dataset:
- Same test set
- Same image size
- Same confidence threshold
- Same IoU threshold

Evaluation metrics:
- Precision
- Recall
- mAP50
- mAP50-95

---

# Overall Performance

| Model | Epochs | Precision | Recall | mAP50 | mAP50-95 |
|--------|-------:|----------:|--------:|-------:|----------:|
| YOLO11s | 20 | 0.9788 | 0.9817 | 0.9877 | 0.5828 |
| YOLO26n | 20 | 0.9449 | 0.9567 | 0.9795 | 0.5344 |
| YOLO26m | 11 | 0.9739 | 0.9808 | 0.9882 | 0.5462 |

---

# Training Curves

## YOLO11s

### Results Curve

![results](../runs/yolo11/results.png)

---

## YOLO26n

![results](../runs/yolo26n/results.png)

---

## YOLO26m

![results](../runs/yolo26m/results.png)

---

# Confusion Matrix

## YOLO11

![confusion](../runs/yolo11/confusion_matrix.png)

---

## YOLO26n

![confusion](../runs/yolo26n/confusion_matrix.png)

---

## YOLO26m

![confusion](../runs/yolo26m/confusion_matrix.png)

---

# Precision-Recall Curve

## YOLO11s

![PR](../runs/yolo11/PR_curve.png)

---

## YOLO26n

![PR](../runs/yolo26n/BoxPR_curve.png)

---

## YOLO26m

![PR](../runs/yolo26m/BoxPR_curve.png)

---

# F1 Curve

## YOLO11s

![F1](../runs/yolo11/F1_curve.png)

---


## YOLO26n

![F1](../runs/yolo26n/BoxF1_curve.png)

---

## YOLO26m

![F1](../runs/yolo26m/BoxF1_curve.png)

---

# Precision Curve

## YOLO11

![Precision](../runs/yolo11/P_curve.png)

---

## YOLO26n

![Precision](../runs/yolo26n/BoxP_curve.png)

---

## YOLO26m

![Precision](../runs/yolo26m/BoxP_curve.png)

---

# Recall Curve

## YOLO11

![Recall](../runs/yolo11/R_curve.png)

---

## YOLO26n

![Recall](../runs/yolo26n/BoxR_curve.png)

---

## YOLO26m

![Recall](../runs/yolo26m/BoxR_curve.png)

---

# Validation Predictions

## Sample 1

### Ground Truth

![Ground truth](../runs/yolo11/val_batch0_labels.jpg)

### YOLO11

![YOLO11 prediction](../runs/yolo11/val_batch0_pred.jpg)

### YOLO26n

![YOLO26n prediction](../runs/yolo26n/val_batch0_pred.jpg)

### YOLO26m

![YOLO26m prediction](../runs/yolo26m/val_batch0_pred.jpg)

---

## Sample 2

### Ground Truth

![Ground truth](../runs/yolo11/val_batch1_labels.jpg)

### YOLO11

![YOLO11 prediction](../runs/yolo11/val_batch1_pred.jpg)

### YOLO26n

![YOLO26n prediction](../runs/yolo26n/val_batch1_pred.jpg)

### YOLO26m

![YOLO26m prediction](../runs/yolo26m/val_batch1_pred.jpg)

---

---

# Understanding the mAP50 / mAP50-95 Gap

All three models show a large gap between mAP50 (~0.98) and mAP50-95 (~0.53–0.58). This is expected and worth explaining directly:

- **mAP50** evaluates detections at a single, lenient IoU threshold (0.5) — a prediction only needs to overlap the ground truth box by 50% to count as correct.
- **mAP50-95** averages performance across ten stricter thresholds (0.5 to 0.95), requiring much tighter box-boundary precision.

The gap indicates the models are reliably **finding** defects but less precise at **tightly localizing** their exact boundaries. This is a common pattern for small or thin defect classes — Mouse Bite and Spur in particular are small, irregularly-shaped defects where a few pixels of boundary error represents a much larger relative error than on a bigger object. This doesn't indicate a training failure; it reflects the inherent difficulty of pixel-precise localization on small defect geometries, and is consistent across all three architectures tested.

---

# Reading the Curves

- **Precision-Recall curve**: shows the tradeoff between precision and recall as the confidence threshold varies. A curve staying close to the top-right corner indicates strong performance across most threshold settings, not just one cherry-picked value.
- **F1 curve**: identifies the confidence threshold that best balances precision and recall — useful for choosing an actual operating threshold for deployment, rather than reporting metrics at an arbitrary default.
- **Confusion matrix**: shows which defect classes are most often confused with each other, useful for diagnosing whether errors are concentrated in specific visually-similar defect types (e.g. Mouse Bite vs Spur, both small edge-boundary defects).

Full results interpretation, model comparison, and conclusions are covered in `08_results.md` and `09_yolo11_vs_yolo26.md`.