from .base_detector_model import BaseDetectorModel
import object_detector as obj_det

class MobileNetDetector(BaseDetectorModel):
    def __init__(self, labels = []):
        super().__init__()
        
    def add_labels(self, labels):
        pass

    def encode_labels(self, labels):
        pass

    def load_model(self):
        pass

    def detect_objects(self, image):
        pass