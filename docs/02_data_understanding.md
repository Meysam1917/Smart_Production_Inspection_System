# Data Understanding

## Dataset Overview

Dataset Name:
PCB Defect Dataset

Domain:
Industrial Quality Inspection

Task:
Instance Segmentation

## Dataset Structure

Train Images: 8534

Validation Images: 1066

Test Images: 1068

Total Images: 10668

## Classes

| Class | Instances |
|--------|----------:|
| mouse_bite | 3684 |
| spur | 3636 |
| missing_hole | 3612 |
| short | 3508 |
| open_circuit | 3548 |
| spurious_copper | 3676 |

Total Instances: 21664

## Class Distribution

The dataset is well balanced.

The difference between the largest and the smallest class is approximately 5%, therefore no class balancing techniques are currently required.

(Insert class distribution figure here)

## Annotation Format

YOLO Segmentation

Each object is represented by a polygon annotation.

## Initial Dataset Inspection

The dataset contains:

- Training set
- Validation set
- Test set

No missing split was observed.

Labels appear correctly formatted.

## Strengths

- Large number of images
- Balanced classes
- Pixel-level annotations
- Industrial domain
- Ready-to-use train/validation/test split

## Weaknesses

- Yet to inspect image quality manually.
- Yet to verify annotation accuracy on random samples.

## Why this dataset?

This dataset was selected because it provides:

- Real industrial inspection data.
- High-quality segmentation annotations.
- Balanced class distribution.
- Enough samples for deep learning training.