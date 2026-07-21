# Data Preparation

## Dataset

PCB Defect Dataset

## Dataset Structure

```
dataset/
│
├── train/
├── val/
└── test/
```

## Classes

- mouse_bite
- spur
- missing_hole
- short
- open_circuit
- spurious_copper

## Image Resolution

(To be filled after inspection)

## Annotation Format

YOLO Object Detection Format

Each annotation file contains one line per object:
<class_id> <x_center> <y_center> <width> <height>

All coordinates are normalized to the image dimensions.

## Data Quality

- No missing labels observed.
- Balanced class distribution.
- Train/Validation/Test split already provided.

## Preprocessing

- Image size: 640 × 640
- Normalization: Performed automatically by Ultralytics
- Polygon annotations converted automatically during training

## Data Augmentation

YOLO default augmentations:

- Mosaic
- Flip
- Scale
- HSV augmentation
- Translation
- Perspective

## Why no additional preprocessing?

The dataset is already balanced and well annotated.
Therefore, no oversampling or manual balancing techniques were required.