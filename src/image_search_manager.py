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
        self.__output_formatter = OutputFormatter()
        self.__object_detection = ObjectDetection()
        self.__index_access = IndexAccess()
        self.__image_access = ImageAccess()
        self.__matching_engine = MatchingEngine()

    def add(self, image_path) -> str:
        self.__index_access.add_image_path(image_path)
        image_data = self.__image_access.read_image(image_path)
        detected_objects = self.__object_detection.detect_objects(image_data)
        self.__index_access.add_detected_objects(image_path, detected_objects)