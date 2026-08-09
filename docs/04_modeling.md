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

After completing the baseline system with YOLO11, a second experiment was conducted using the YOLO26 architecture to evaluate whether the newer model could improve detection performance on the same dataset.

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

The YOLO26n model used the same 20-epoch schedule with output folder `runs/yolo26n`.

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

## Experimental Setup

All three experiments used the same:

- PCB defect dataset
- Train / Validation / Test split
- Image resolution (640 × 640)
- Data augmentation strategy
- Evaluation metrics

This ensures that performance differences originate from the model architecture rather than the dataset or preprocessing pipeline.

---

## Hardware

Training was performed on a personal laptop equipped with:

- NVIDIA RTX 3060 Laptop GPU (6 GB VRAM)
- Intel Core i9 Processor
- Windows 11

The limited GPU memory introduced several practical constraints during experimentation.

---

## Training Challenges

Unlike the YOLO11 baseline, training YOLO26 required significantly more experimentation to identify stable training parameters.

Several combinations of batch size, number of workers, image size, and memory allocation were tested before reaching a configuration capable of utilizing the GPU efficiently without triggering CUDA memory errors, system warnings, or application crashes.

Finding an optimal configuration required balancing GPU utilization, VRAM consumption, training speed, and overall system stability. This optimization process became an important engineering task beyond simply training the model.

---

## Why Only 11 Epochs for YOLO26m?

The YOLO26m model contains substantially more parameters than the baseline YOLO11 model.

Due to the computational limitations of the available hardware, training was intentionally limited to **11 epochs**.

Although this is shorter than a typical training schedule, it was sufficient to:

- Validate the training pipeline
- Observe convergence behavior
- Compare learning trends with YOLO11
- Perform an initial evaluation of the new architecture

Longer training would likely improve performance but exceeded the practical limits of the available hardware.

---

## Modeling Summary

Object detection was chosen because PCB inspection requires defect localization, classification, multiple detections per image, and per-prediction confidence scoring.

Three architectures were evaluated under identical experimental conditions to compare accuracy, robustness, and deployment efficiency. Results and model selection guidance are covered in `05_evaluation.md`.
