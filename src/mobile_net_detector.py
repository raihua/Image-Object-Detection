from base_detector_model import BaseDetectorModel
import object_detector as obj_det


class MobileNetDetector(BaseDetectorModel):
    def __init__(self):
        self.__model_path = obj_det.DETECTION_MODEL_DIR

    def add_labels(self, labels):
        last_key = max(obj_det.ALL_LABELS.keys())
        for label in labels:
            last_key += 1
            obj_det.ALL_LABELS[last_key] = label
        print(obj_det.ALL_LABELS)

    def encode_labels(self, labels):
        obj_det.encode_labels(labels)

    def load_model(self):
        pass
    
    def detect_objects(self, image):
        pass
