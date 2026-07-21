from .inspection_manager import InspectionManager
from .decision_engine import DecisionEngine
from .inspection_report import InspectionReport
from .result_converter import ResultConverter

class InspectionPipeline:
    def __init__(self, detector, converter, manager, decision_engine, report_generator, visualizer):
        self.detector = detector
        self.converter = converter
        self.manager = manager
        self.decision_engine = decision_engine
        self.report_generator = report_generator
        self.visualizer = visualizer

    def Process(self, image):
        self.manager.clear()

        results = self.detector.detect(image)
        defects = self.converter.convert(results)

        self.manager.add_defects(defects)
        all_defects = self.manager.get_all_defect()

        inspection_result = self.decision_engine.decide(all_defects)

        report = self.report_generator.generate(all_defects, inspection_result)
        output_image = self.visualizer.draw(
            image, all_defects, inspection_result)

        return report, output_image
