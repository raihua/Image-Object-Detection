from base_detector_model import BaseDetectorModel
import importlib as il


class MobileNetDetector(BaseDetectorModel):
    def __init__(self):
        super().__init__()
        self.__wrappee = il.import_module("object_detector")

    def add_labels(self, labels):
        last_key = max(self.__wrappee.ALL_LABELS.keys())
        for label in labels:
            last_key += 1
            self.__wrappee.ALL_LABELS[last_key] = label

    def get_labels(self) -> dict:
        return self.__wrappee.ALL_LABELS

    def encode_labels(self, labels) -> list:
        return self.__wrappee.encode_labels(labels)

    def load_model(self):
        return self.__wrappee.load_model()

    def detect_objects(self, image) -> set:
        return self.__wrappee.detect_objects(image)
