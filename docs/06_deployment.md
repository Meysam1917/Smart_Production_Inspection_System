# Deployment

## Pipeline

Image → YOLO Detector → ResultConverter → InspectionManager → DecisionEngine → InspectionReport → Visualizer

---

## Current Deployment Mode

The system currently runs as a local batch-inference pipeline: images are processed one at a time through `main.py`, producing a JSON report and annotated image per input. This suits offline QA review or manual spot-checking, but is not yet structured for a live production line.

---

## Path to Production Deployment

To move from local script execution to a real inspection-line deployment, the following would be needed:

- **API layer (FastAPI):** wrap the existing pipeline behind a `/inspect` endpoint accepting an image and returning the JSON report, so the pipeline can be called from other systems (a line-camera controller, a MES/quality database, a dashboard) instead of run manually.
- **Containerization (Docker):** package the model weights, dependencies, and pipeline into a container for consistent deployment across machines/environments — removes "works on my machine" risk.
- **Real-time / streaming inference:** industrial lines typically require processing a continuous camera feed rather than single static images, which would mean adapting the pipeline to a video/stream input with frame-level throughput considerations (batching, latency budget).
- **Model serving optimization:** TensorRT or ONNX export for faster inference latency in a production setting, particularly relevant since PCB inspection at line-speed has real-time constraints.
- **Logging/persistence:** inspection results currently write to local JSON; a production system would log to a database for traceability and audit history.

---

## Output

- Annotated Image
- JSON Report
- Inspection Decision (PASS / REWORK / REJECT)