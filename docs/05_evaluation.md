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

## Overall Performance

| Model | Epochs | Precision | Recall | mAP50 | mAP50-95 |
|--------|-------:|----------:|--------:|-------:|----------:|
| YOLO11s | 20 | 0.9788 | 0.9817 | 0.9877 | 0.5828 |
| YOLO26n | 20 | 0.9449 | 0.9567 | 0.9795 | 0.5344 |
| YOLO26m | 11 | 0.9739 | 0.9808 | 0.9882 | 0.5462 |

![Comparison](assets/samples/model_comparison.png)

All three architectures deliver strong detection quality. YOLO26m slightly leads on mAP50 despite the shorter 11-epoch schedule. YOLO11s achieves the best performance across stricter IoU thresholds (mAP50-95). YOLO26n is the best choice when deployment efficiency is the priority.

---

## Model Comparison Discussion

The experiments show that YOLO26m delivers the highest accuracy in this setup, despite the shorter training schedule. YOLO11s remains the most robust model across stricter IoU thresholds. YOLO26n offers a favorable balance between accuracy and resource usage, but produces noticeably more per-image errors than the other two models.

The comparison reinforces the need to choose a model based on the target deployment scenario rather than a single metric alone.

---

## Training Curves

### YOLO11s

![results](assets/yolo11/results.png)

### YOLO26n

![results](assets/yolo26n/results.png)

### YOLO26m

![results](assets/yolo26m/results.png)

---

## Confusion Matrix

### YOLO11s

![confusion](assets/yolo11/confusion_matrix.png)

### YOLO26n

![confusion](assets/yolo26n/confusion_matrix.png)

### YOLO26m

![confusion](assets/yolo26m/confusion_matrix.png)

---

## Precision-Recall Curve

### YOLO11s

![PR](assets/yolo11/PR_curve.png)

### YOLO26n

![PR](assets/yolo26n/BoxPR_curve.png)

### YOLO26m

![PR](assets/yolo26m/BoxPR_curve.png)

---

## F1 Curve

### YOLO11s

![F1](assets/yolo11/F1_curve.png)

### YOLO26n

![F1](assets/yolo26n/BoxF1_curve.png)

### YOLO26m

![F1](assets/yolo26m/BoxF1_curve.png)

---

## Precision Curve

### YOLO11s

![Precision](assets/yolo11/P_curve.png)

### YOLO26n

![Precision](assets/yolo26n/BoxP_curve.png)

### YOLO26m

![Precision](assets/yolo26m/BoxP_curve.png)

---

## Recall Curve

### YOLO11s

![Recall](assets/yolo11/R_curve.png)

### YOLO26n

![Recall](assets/yolo26n/BoxR_curve.png)

### YOLO26m

![Recall](assets/yolo26m/BoxR_curve.png)

---

## Validation Predictions

### Sample 1

#### Ground Truth

![Ground truth](assets/yolo11/val_batch0_labels.jpg)

#### YOLO11s

![YOLO11 prediction](assets/yolo11/val_batch0_pred.jpg)

#### YOLO26n

![YOLO26n prediction](assets/yolo26n/val_batch0_pred.jpg)

#### YOLO26m

![YOLO26m prediction](assets/yolo26m/val_batch0_pred.jpg)

The model correctly detects multiple defect regions and matches the annotated bounding boxes for the sample image.

---

### Sample 2

#### Ground Truth

![Ground truth](assets/yolo11/val_batch1_labels.jpg)

#### YOLO11s

![YOLO11 prediction](assets/yolo11/val_batch1_pred.jpg)

#### YOLO26n

![YOLO26n prediction](assets/yolo26n/val_batch1_pred.jpg)

#### YOLO26m

![YOLO26m prediction](assets/yolo26m/val_batch1_pred.jpg)

The detector maintains high recall on the second validation sample, recovering small defect instances with accurate localization.

---

### Sample 3 (YOLO26m)

#### Ground Truth

![Ground truth](assets/yolo26m/val_batch2_labels.jpg)

#### YOLO26m Prediction

![Prediction](assets/yolo26m/val_batch2_pred.jpg)

The third example shows robust detection in a more cluttered board layout, with few false positives.

---

## Understanding the mAP50 / mAP50-95 Gap

All three models show a large gap between mAP50 (~0.98) and mAP50-95 (~0.53–0.58). This is expected and worth explaining directly:

- **mAP50** evaluates detections at a single, lenient IoU threshold (0.5) — a prediction only needs to overlap the ground truth box by 50% to count as correct.
- **mAP50-95** averages performance across ten stricter thresholds (0.5 to 0.95), requiring much tighter box-boundary precision.

The gap indicates the models are reliably **finding** defects but less precise at **tightly localizing** their exact boundaries. This is a common pattern for small or thin defect classes — Mouse Bite and Spur in particular are small, irregularly-shaped defects where a few pixels of boundary error represents a much larger relative error than on a bigger object. This doesn't indicate a training failure; it reflects the inherent difficulty of pixel-precise localization on small defect geometries, and is consistent across all three architectures tested.

---

## Reading the Curves

- **Precision-Recall curve**: shows the tradeoff between precision and recall as the confidence threshold varies. A curve staying close to the top-right corner indicates strong performance across most threshold settings, not just one cherry-picked value.
- **F1 curve**: identifies the confidence threshold that best balances precision and recall — useful for choosing an actual operating threshold for deployment, rather than reporting metrics at an arbitrary default.
- **Confusion matrix**: shows which defect classes are most often confused with each other, useful for diagnosing whether errors are concentrated in specific visually-similar defect types (e.g. Mouse Bite vs Spur, both small edge-boundary defects).

---

## Error Analysis

Beyond aggregate metrics (Precision, Recall, mAP), individual wrong detections were inspected to understand *why* errors happen and what could reduce them. Errors were computed per-image using a custom IoU-matching script (`tools/error_analyzer.py`) at IoU threshold 0.5.

### Error Summary by Model

| Model | Test Images | Images w/ Errors | True Positives | False Positives | False Negatives |
|---|---:|---:|---:|---:|---:|
| YOLO11s | 1068 | 72 (6.7%) | 1642 | 61 | 20 |
| YOLO26n | 1068 | 175 (16.4%) | 1610 | 157 | 52 |
| YOLO26m | 1068 | 79 (7.4%) | 1640 | 65 | 22 |

YOLO26n has noticeably more errors than the other two models — both more false positives (extra/wrong detections) and more false negatives (missed defects). This is consistent with it having the lowest Precision and Recall in the official evaluation above, and matches expectations for the lightweight "nano" variant.

YOLO11s and YOLO26m perform similarly on error counts, despite YOLO26m being trained for only 11 epochs vs YOLO11s's 20 — suggesting YOLO26m's architecture reaches strong performance faster.

### Confirmed Findings

The three `results-*.txt` files were parsed in full — every individual false positive and false negative, across all three models, categorized by defect class and confidence score.

![Findings](assets/samples/fp_by_class.png)

#### 1. Spurious Copper and Short dominate false positives

| Model | Top FP classes (count) |
|---|---|
| YOLO11s | Short (21), Spurious Copper (14), Mouse Bite (11), Missing Hole (7) |
| YOLO26n | Spurious Copper (50), Short (38), Spur (25), Missing Hole (19) |
| YOLO26m | Spurious Copper (19), Short (13), Mouse Bite (12), Missing Hole (10) |

Both defect types are visually defined by irregular copper-colored shapes/traces on the board, which can appear in normal board texture, solder traces, and copper pours.

#### 2. Spur is the most consistently missed defect

| Model | Top FN classes (count) |
|---|---|
| YOLO11s | Spur (7), Spurious Copper (5), Open Circuit (5) |
| YOLO26n | Spurious Copper (13), Spur (12), Short (11) |
| YOLO26m | Spur (8), Spurious Copper (5), Short (4) |

Spur defects are thin, sharp protrusions — among the smallest and most geometrically subtle defect types in this dataset.

#### 3. Most false positives are near-hallucinations, not localization errors

Across all three models, the overwhelming majority of false positives have `best_iou = 0.00` — meaning the model detected a defect in a location with **no ground truth defect at all**. Only 2–5 false positives per model (out of 61–157) had any partial box overlap.

#### 4. YOLO26n's false positives are disproportionately low-confidence

| Model | FP mean confidence | FP with confidence < 0.5 |
|---|---|---|
| YOLO11s | 0.51 | 44% |
| YOLO26n | 0.43 | **73%** |
| YOLO26m | 0.54 | 46% |

A higher confidence threshold at inference specifically benefits YOLO26n, likely filtering out a large share of its false positives with comparatively little cost to recall.

#### 5. Certain images fail for every model

Some file names appear as errors in all three logs — e.g. `l_light_04_spur_05_2_600.jpg`, `rotation_270_light_01_short_18_1_600.jpg`, `rotation_270_light_01_open_circuit_13_3_600.jpg`. These are architecture-independent failures — the issue may live in the image/label itself rather than in any one model's weaknesses.

### Recommendations to Reduce Errors

1. **Raise the inference confidence threshold, especially for YOLO26n.** Use the F1 curve above to pick a threshold that maximizes F1.
2. **Add hard-negative training examples for Spurious Copper and Short.** The model needs more exposure to normal copper traces and solder regions without a defect label.
3. **Investigate Spur detection specifically.** Consider increasing input resolution (`imgsz` above 640) or reviewing Spur training example quality.
4. **Manually review cross-model failure images.** Architecture-independent failures may reveal annotation quality issues.
5. **Post-processing tuning won't fix hallucinated detections.** The false positives are in the wrong location entirely — better negative examples matter more than NMS tuning.

### Tooling

Error analysis was performed using `tools/error_analyzer.py`, which runs inference on the test set, matches predictions to ground truth boxes via IoU (threshold 0.5), and saves annotated images for every image containing at least one error.

---

## Future Work

- Longer YOLO26m training to close the gap with YOLO11s on mAP50-95
- Hyperparameter optimization (learning rate schedule, augmentation strength)