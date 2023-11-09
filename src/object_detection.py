from mobile_net_detector import MobileNetDetector
from numpy import ndarray

class ObjectDetection:
    def __init__(self, detector_model):
        self.__detector_model  = detector_model

    def get_model(self):
        return self.__detector_model
    
    def set_model(self, model):
        self.__detector_model = model

    def add_labels(self, labels):
        return self.__detector_model.add_labels(labels)
    
    def get_labels(self):
        return self.__detector_model.get_labels(self)

    def encode_labels(self, labels):
        return self.__detector_model.encode_labels(labels)

    def load_model(self):
        return self.__detector_model.load_model()

    def detect_objects(self, image):
        return self.__detector_model.detect_objects(image)

    detector_model = property(get_model, set_model)