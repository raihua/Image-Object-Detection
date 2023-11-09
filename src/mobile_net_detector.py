from base_detector_model import BaseDetectorModel
import object_detector as obj_det


class MobileNetDetector(BaseDetectorModel):
    def add_labels(self, labels):
        last_key = max(obj_det.ALL_LABELS.keys())
        for label in labels:
            last_key += 1
            obj_det.ALL_LABELS[last_key] = label

    def encode_labels(self, labels):
        obj_det.encode_labels(labels)

    def load_model(self):
        obj_det.load_model()

    def detect_objects(self, image):
        obj_det.detect_objects(image)
