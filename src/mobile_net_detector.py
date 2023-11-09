from base_detector_model import BaseDetectorModel
import object_detector as obj_det


class MobileNetDetector(BaseDetectorModel):
    def __init__(self):
        self.__wrappee = obj_det
    
    def add_labels(self, labels):
        last_key = max(self.__wrappee.ALL_LABELS.keys())
        for label in labels:
            last_key += 1
            self.__wrappee.ALL_LABELS[last_key] = label

    def encode_labels(self, labels):
        self.__wrappee.encode_labels(labels)

    def load_model(self):
        self.__wrappee.load_model()

    def detect_objects(self, image):
        self.__wrappee.detect_objects(image)

