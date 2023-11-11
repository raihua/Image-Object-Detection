from output_formatter import OutputFormatter
from object_detection import ObjectDetection
from index_access import IndexAccess
from image_access import ImageAccess
from matching_engine import MatchingEngine

from num_descending_format import NumDescendingFormat
from alphabetical_ascending_format import AlphabeticalAscendingFormat
from sqlite_indexing import SQLiteIndexing
from mobile_net_detector import MobileNetDetector
from cosine_similarity import CosineSimilarity

import sqlite3


class ImageSearchManager:
    def __init__(self):
        self.__output_formatter = OutputFormatter()
        self.__object_detection = ObjectDetection()
        self.__index_access = IndexAccess()
        self.__image_access = ImageAccess()
        self.__matching_engine = MatchingEngine()

        self.__index_access.set_strategy(SQLiteIndexing(sqlite3.connect(":memory:")))
        self.__object_detection.set_model(MobileNetDetector())

    def add(self, image_path) -> str:
        self.__index_access.add_image_path(image_path)
        image_data = self.__image_access.read_image(image_path)
        detected_objects = sorted(self.__object_detection.detect_objects(image_data))
        self.__index_access.add_detected_objects(image_path, detected_objects)
        result_str = "Detected objects " + ",".join(detected_objects)
        return result_str

    def search(self, option, terms) -> str:
        result_img_objects = None
        if option:
            result_img_objects = self.__index_access.get_images_with_all_objects(terms)
        else:
            result_img_objects = self.__index_access.get_images_with_some_objects(terms)

        self.__output_formatter.set_strategy(AlphabeticalAscendingFormat())
        result_str = self.__output_formatter.format_data(result_img_objects)
        result_str += f"\n{len(result_img_objects)} matches found."
        return result_str

    def similar(self, k, image_path):
        self.__output_formatter.set_strategy(NumDescendingFormat())
        self.__matching_engine.set_strategy(CosineSimilarity())

        all_images_objects = self.__index_access.get_all_images_and_objects()

        image_data = self.__image_access.read_image(image_path)
        objects_detected = self.__object_detection.detect_objects(image_data)
        encoded_objects = self.__object_detection.encode_labels(objects_detected)

        
        encoded_images_data = [(path, [self.__object_detection.encode_labels(label) for label in objects]) for path, objects in all_images_objects]

        
        matching_results = self.__matching_engine.execute_matching(
            encoded_objects, encoded_images_data
        )
        result_str = self.__output_formatter.format_data(matching_results, k)
        return result_str
