# Data Preparation

## Annotation Format

YOLO Detection Format

Each annotation contains

<class_id> <x_center> <y_center> <width> <height>

---

## Image Resolution

640 × 640

---

## Data Split

Train
Validation
Test

---

## Why this dataset?

The dataset contains multiple PCB defects with sufficient class balance and predefined train/validation/test splits.

---

## Data Augmentation

YOLO default augmentations

- Mosaic
- Flip
- Scale
- HSV augmentation

---

## Preprocessing

- Image resizing
- Label validation
- Dataset integrity verification