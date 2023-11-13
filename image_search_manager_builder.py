from output_formatter import OutputFormatter
from object_detection import ObjectDetection
from index_access import IndexAccess
from image_access import ImageAccess
from matching_engine import MatchingEngine
from image_search_manager import ImageSearchManager

class ImageSearchManagerBuilder:
    def __init__(self):
        self.output_formatter = OutputFormatter()
        self.object_detection = ObjectDetection()
        self.index_access = IndexAccess()
        self.image_access = ImageAccess()
        self.matching_engine = MatchingEngine()

    def set_index_strategy(self, strategy):
        self.index_access.set_strategy(strategy)
        return self

    def set_object_detection_model(self, model):
        self.object_detection.set_model(model)
        return self
    
    def set_matching_strategy(self, strategy):
        self.matching_engine.set_strategy(strategy)
        return self


    def build(self):
        return ImageSearchManager(self.output_formatter, self.object_detection, self.index_access, self.image_access, self.matching_engine)