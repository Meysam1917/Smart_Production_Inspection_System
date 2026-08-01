# YOLO11 vs YOLO26 Comparison

## Objective

After completing the baseline PCB inspection system using YOLO11, a second experiment was conducted using the newly released YOLO26 architecture to evaluate whether the newer model could improve detection performance on the same dataset.

The primary goals of this experiment were:

- Compare detection performance.
- Evaluate inference quality.
- Measure training stability.
- Analyze computational requirements.

---

# Experimental Setup

Both experiments used the same:

- PCB defect dataset
- Train / Validation / Test split
- Image resolution
- Data augmentation strategy
- Evaluation metrics

This ensures that performance differences originate from the model architecture rather than the dataset or preprocessing pipeline.

---

# Hardware

Training was performed on a personal laptop equipped with:

- NVIDIA RTX 3060 Laptop GPU (6 GB VRAM)
- Intel Core i9 Processor
- Windows 11

The limited GPU memory introduced several practical constraints during experimentation.

---

# Training Challenges

Unlike the YOLO11 baseline, training YOLO26 required significantly more experimentation to identify stable training parameters.

Several combinations of:

- Batch size
- Number of workers
- Image size
- Memory allocation

were tested before reaching a configuration capable of utilizing the GPU efficiently without triggering CUDA memory errors, system warnings, or application crashes.

Finding an optimal configuration required balancing:

- GPU utilization
- VRAM consumption
- Training speed
- Overall system stability

This optimization process became an important engineering task beyond simply training the model.

---

# Why Only 11 Epochs?

The **YOLO26m** model contains substantially more parameters than the baseline YOLO11 model.

Due to the computational limitations of the available hardware, training was intentionally limited to **11 epochs**.

Although this is shorter than a typical training schedule, it was sufficient to:

- Validate the training pipeline.
- Observe convergence behavior.
- Compare learning trends with YOLO11.
- Perform an initial evaluation of the new architecture.

Longer training would likely improve performance but exceeded the practical limits of the available hardware.

---

# Results

## YOLO11s

Trained for 20 epochs, the YOLO11s baseline achieved strong detection performance on the PCB dataset.

| Metric | Value |
|---------|------:|
| Precision | 0.9788 |
| Recall | 0.9817 |
| mAP50 | 0.9877 |
| mAP50-95 | 0.5828 |

---

## YOLO26n

The YOLO26n model also trained for 20 epochs and offered a lightweight alternative with competitive accuracy.

| Metric | Value |
|---------|------:|
| Precision | 0.9449 |
| Recall | 0.9567 |
| mAP50 | 0.9795 |
| mAP50-95 | 0.5344 |

---

## YOLO26m

The YOLO26m model was trained for 11 epochs due to hardware constraints and still achieved the best mAP50 of the experiment.

| Metric | Value |
|---------|------:|
| Precision | 0.9739 |
| Recall | 0.9808 |
| mAP50 | 0.9882 |
| mAP50-95 | 0.5462 |

---

# Discussion

The experiments show that YOLO26m delivers the highest accuracy in this setup, despite the shorter 11-epoch training schedule. YOLO11s remains the most robust model across stricter IoU thresholds, as evidenced by its top mAP50-95 value. YOLO26n is the best choice when deployment efficiency is the priority, offering a favorable balance between accuracy and resource usage.

The comparison reinforces the need to choose a model based on the target deployment scenario: highest accuracy (`YOLO26m`), strongest strict-IoU generalization (`YOLO11s`), or lightweight inference (`YOLO26n`).

---

# Future Work

The experiments demonstrate the trade-off between model complexity and computational cost.

Smaller models offer:

- Faster training
- Lower memory consumption
- Easier deployment

Larger models generally provide greater representational capacity but require significantly more computational resources and longer training times.

The comparison highlights that selecting a model for industrial deployment should consider not only detection accuracy but also hardware constraints, inference speed, and deployment requirements.

---

# Future Work

Future experiments may include:

- Longer YOLO26m training
- Hyperparameter optimization
- Mixed precision training
- Cross-validation
- TensorRT optimization
- Deployment benchmarking