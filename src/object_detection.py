from mobile_net_detector import MobileNetDetector
from numpy import ndarray

class ObjectDetection:
    def __init__(self, detector_model = MobileNetDetector):
        self.__detector_model = detector_model

    def get_model(self):
        return self.__detector_model
    
    def set_model(self, model):
        self.__detector_model = model

    detector_model = property(get_model)