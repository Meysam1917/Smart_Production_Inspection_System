# AI-Based PCB Inspection System

An automated PCB (Printed Circuit Board) visual inspection system developed using **YOLO11** and **Python**. The system detects manufacturing defects, evaluates PCB quality using a rule-based scoring engine, and generates inspection reports with annotated images.

---

## Features

- Automatic PCB defect detection
- Six supported defect classes
- Quality score calculation
- PASS / REWORK / REJECT decision
- JSON inspection report generation
- Annotated output images
- Modular software architecture
- CRISP-DM based development process

---

## Supported Defects

| Defect |
|---------|
| Mouse Bite |
| Spur |
| Missing Hole |
| Open Circuit |
| Short |
| Spurious Copper |

---

## Project Architecture

```
Input Image
      │
      ▼
YOLO Detector
      │
      ▼
Result Converter
      │
      ▼
PCBDefect Objects
      │
      ▼
Inspection Manager
      │
      ▼
Decision Engine
      │
      ▼
Inspection Report
      │
      ▼
Visualizer
```

---

## Dataset

Dataset used:

PCB Defect Detection Dataset

Classes:

- Mouse Bite
- Spur
- Missing Hole
- Open Circuit
- Short
- Spurious Copper

Dataset statistics:

- Train Images: 8534
- Validation Images: 1066
- Test Images: 1068

Total defect instances:

21664

---

## Technologies

- Python
- Ultralytics YOLO11
- OpenCV
- NumPy

---

## Results

Model Performance

| Metric | Value |
|---------|-------|
| Precision | 0.98 |
| Recall | 0.99 |
| mAP50 | 0.99 |
| mAP50-95 | 0.58 |

---

## Project Structure

```
SmartProduceInspectionSystem/

docs/
models/
reports/
src/
tools/

README.md
requirements.txt
```

---

## Installation

```bash
git clone <repository-url>

cd SmartProduceInspectionSystem

pip install -r requirements.txt
```

---

## Usage

Train

```bash
python src/train.py
```

Run Inspection

```bash
python src/main.py
```

---

## Sample Output

The system generates:

- Annotated PCB image
- Inspection report (JSON)

Example:

```json
{
    "quality_score": 82,
    "status": "REWORK",
    "total_defects": 2
}
```

---

## Development Methodology

The project follows the **CRISP-DM** framework.

- Business Understanding
- Data Understanding
- Data Preparation
- Modeling
- Evaluation
- Deployment

Documentation is available inside the **docs** directory.

---

## Future Improvements

- Instance Segmentation
- Real-time Video Inspection
- Industrial Camera Support
- Streamlit Dashboard
- Confidence-aware Quality Scoring
- Database Logging