# Modeling

## Why Object Detection?

A PCB may contain multiple defects simultaneously.

Image classification cannot localize defects.

Object detection identifies

- location
- class
- confidence

for every defect.

---

## Why YOLO11?

YOLO11 offers

- high inference speed
- strong detection accuracy
- lightweight deployment
- industrial suitability

---

## Training Configuration

The baseline YOLO11s model was trained with the following configuration:

- Epochs: 20
- Batch size: 16
- Optimizer: auto (Ultralytics default)
- Initial learning rate: 0.01
- Image size: 640 × 640
- GPU: CUDA device 0
- Workers: 8
- Mixed precision: enabled (AMP)
- IoU threshold: 0.7
- Output project folder: `runs/yolo11`

The YOLO26m experiment used a smaller training schedule due to hardware constraints:

- Epochs: 11
- Batch size: 8
- Image size: 640 × 640
- Device: 0
- Workers: 8
- Project folder: `runs/yolo26m`

---

## Model Variants

### YOLO11s

Selected as the baseline due to its fast inference speed, lightweight deployment profile, and strong performance on PCB detection tasks. YOLO11s is suitable for environments where resource efficiency is important.

### YOLO26n

A smaller YOLO26 variant evaluated for efficient inference and lower memory usage. It trades a small amount of detection accuracy for a more compact model size.

### YOLO26m

A larger YOLO26 variant evaluated for higher accuracy. The experiment showed that YOLO26m can outperform the baseline in mAP50 even with a limited 11-epoch training schedule.

---

## Modeling Summary

Object detection was chosen because PCB inspection requires:

- defect localization
- defect classification
- multiple detections per image
- confidence scoring for each prediction

The chosen YOLO architectures support these requirements while providing a practical balance of accuracy, speed, and deployment readiness.
