from src.base_detector_model import BaseDetectorModel
import src.object_detector as obj_det


class MobileNetDetector(BaseDetectorModel):
    def __init__(self):
        self.__all_labels = obj_det.ALL_LABELS
        self.__model_path = obj_det.DETECTION_MODEL_DIR

    def add_labels(self, labels):
        for label in labels:
            new_key = max(self.__all_labels.keys()) + 1
            self.__all_labels[new_key] = label

    def get_labels(self):
        return self.__all_labels

    def encode_labels(self, labels):
        obj_det.encode_labels(labels)
