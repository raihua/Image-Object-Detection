from src.output_formatter import OutputFormatter
from src.object_detection import ObjectDetection
from src.index_access import IndexAccess
from src.image_access import ImageAccess
from src.matching_engine import MatchingEngine
from src.image_search_manager import ImageSearchManager

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