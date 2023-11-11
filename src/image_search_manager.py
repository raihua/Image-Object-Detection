from output_formatter import OutputFormatter
from object_detection import ObjectDetection
from index_access import IndexAccess
from image_access import ImageAccess
from matching_engine import MatchingEngine

from num_descending_format import NumDescendingFormat
from alphabetical_ascending_format import AlphabeticalAscendingFormat
from sqlite_indexing import SQLiteIndexing
from mobile_net_detector import MobileNetDetector


class ImageSearchManager:
    def __init__(self):
        self.output_formatter = OutputFormatter()
        self.object_detection = ObjectDetection()
        self.index_access = IndexAccess()
        self.image_access = ImageAccess()
        self.matching_engine = MatchingEngine()
