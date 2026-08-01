# Results

## Detection Performance

The final evaluation compared three models on the same PCB defect detection test set.

| Model | Epochs | Precision | Recall | mAP50 | mAP50-95 |
|------|-------:|---------:|--------:|-------:|----------:|
| YOLO11s | 20 | 0.9788 | 0.9817 | 0.9877 | 0.5828 |
| YOLO26n | 20 | 0.9449 | 0.9567 | 0.9795 | 0.5344 |
| YOLO26m | 11 | 0.9739 | 0.9808 | 0.9882 | 0.5462 |

This summary shows that all three architectures deliver strong detection quality, with YOLO26m slightly leading on mAP50 and YOLO11s achieving the best performance across stricter IoU thresholds.

---

## Example 1

### Ground Truth

![Ground truth](../runs/yolo26m/val_batch0_labels.jpg)

### Model Prediction

![Prediction](../runs/yolo26m/val_batch0_pred.jpg)

Description: The model correctly detects multiple defect regions and matches the annotated bounding boxes for the sample image.

---

## Example 2

### Ground Truth

![Ground truth](../runs/yolo26m/val_batch1_labels.jpg)

### Model Prediction

![Prediction](../runs/yolo26m/val_batch1_pred.jpg)

Description: The detector maintains high recall on the second validation sample, recovering small defect instances with accurate localization.

---

## Example 3

### Ground Truth

![Ground truth](../runs/yolo26m/val_batch2_labels.jpg)

### Model Prediction

![Prediction](../runs/yolo26m/val_batch2_pred.jpg)

Description: The third example shows robust detection in a more cluttered board layout, with few false positives.

---

---

## Discussion

The prediction examples above show the detector correctly localizing multiple defect types per board, including in cluttered layouts with several simultaneous defects. Qualitative results align with the quantitative metrics reported in `05_evaluation.md`.

For full model-to-model comparison and architecture selection reasoning, see `09_yolo11_vs_yolo26.md`.