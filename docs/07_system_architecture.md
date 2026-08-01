# System Architecture

The system architecture is organized as a sequential inspection pipeline that converts input PCB images into structured defect reports.

```text
Image
      │
      ▼
YOLO Detector  ──────────►  Runs inference, returns raw
                             Ultralytics detection results
      │
      ▼
Result Converter ─────────► Converts raw YOLO output into
                             application-level PCBDefect objects
      │
      ▼
PCBDefect Objects
      │
      ▼
Inspection Manager ───────► Collects all defects for one board,
                             clears state between images
      │
      ▼
```

---

## Components

### YOLODetector

Runs inference.

---

### ResultConverter

Converts YOLO output into PCBDefect objects.

---

### PCBDefect

Represents one detected defect.

---

### InspectionManager

Stores all defects belonging to one PCB.

---

### DecisionEngine

Calculates quality score and inspection status.

---

### InspectionReport

Creates JSON reports.

---

### Visualizer

Draws detections and inspection results.