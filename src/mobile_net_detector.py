from base_detector_model import BaseDetectorModel
from importlib import import_module


class MobileNetDetector(BaseDetectorModel):
    def __init__(self):
        super().__init__()
        self.__wrappee = import_module("object_detector")

    def add_labels(self, labels):
        last_key = max(self.__wrappee.ALL_LABELS.keys())
        for label in labels:
            last_key += 1
            self.__wrappee.ALL_LABELS[last_key] = label

    def get_labels(self):
        return self.__wrappee.ALL_LABELS

    def encode_labels(self, labels):
        return self.__wrappee.encode_labels(labels)

    def load_model(self):
        return self.__wrappee.load_model()

    def detect_objects(self, image):
        return self.__wrappee.detect_objects(image)
