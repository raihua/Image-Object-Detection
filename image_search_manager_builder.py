from output_formatter import OutputFormatter
from object_detection import ObjectDetection
from index_access import IndexAccess
from image_access import ImageAccess
from matching_engine import MatchingEngine
from image_search_manager import ImageSearchManager

class ImageSearchManagerBuilder:
    def __init__(self):
        self.__output_formatter = OutputFormatter()
        self.__object_detection = ObjectDetection()
        self.__index_access = IndexAccess()
        self.__image_access = ImageAccess()
        self.__matching_engine = MatchingEngine()

    def set_index_strategy(self, strategy):
        self.__index_access.set_strategy(strategy)
        return self

    def set_object_detection_model(self, model):
        self.__object_detection.set_model(model)
        return self
    
    def set_matching_strategy(self, strategy):
        self.__matching_engine.set_strategy(strategy)
        return self


    def build(self):
        return ImageSearchManager(self.__output_formatter, self.__object_detection, self.__index_access, self.__image_access, self.__matching_engine)