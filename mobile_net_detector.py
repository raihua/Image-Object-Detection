from base_detector_model import BaseDetectorModel
import importlib as il


class MobileNetDetector(BaseDetectorModel):
    def __init__(self):
        super().__init__()
        self.detector_module = self.__import_detector_module("object_detector")

    def __import_detector_module(self, module_name):
        try:
            return il.import_module(module_name)
        except ImportError as e:
            raise ImportError(f"Failed to import module '{module_name}': {e}")

    def add_labels(self, labels):
        last_key = max(self.detector_module.ALL_LABELS.keys())
        for label in labels:
            last_key += 1
            self.detector_module.ALL_LABELS[last_key] = label

    def get_labels(self) -> dict:
        return self.detector_module.ALL_LABELS

    def encode_labels(self, labels) -> list:
        return self.detector_module.encode_labels(labels)

    def load_model(self):
        return self.detector_module.load_model()

    def detect_objects(self, image) -> set:
        return self.detector_module.detect_objects(image)
