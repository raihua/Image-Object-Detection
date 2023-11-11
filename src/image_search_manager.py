from src.output_formatter import OutputFormatter
from src.object_detection import ObjectDetection
from src.index_access import IndexAccess
from src.image_access import ImageAccess
from src.matching_engine import MatchingEngine

from src.num_descending_format import NumDescendingFormat
from src.alphabetical_ascending_format import AlphabeticalAscendingFormat
from src.sqlite_indexing import SQLiteIndexing
from src.mobile_net_detector import MobileNetDetector
from src.cosine_similarity import CosineSimilarity

import sqlite3


class ImageSearchManager:
    def __init__(self):
        self.__output_formatter = OutputFormatter()
        self.__object_detection = ObjectDetection()
        self.__index_access = IndexAccess()
        self.__image_access = ImageAccess()
        self.__matching_engine = MatchingEngine()

        self.__index_access.set_strategy(SQLiteIndexing(sqlite3.connect("memory.db")))
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

        
        encoded_all_images_objects = {}
        for path, labels in all_images_objects.items():
            encoded_labels = self.__object_detection.encode_labels(labels)
            encoded_all_images_objects[path] = encoded_labels

        
        matching_results = self.__matching_engine.execute_matching(
            encoded_objects, encoded_all_images_objects
        )

        result_str = self.__output_formatter.format_data(matching_results, k)
        return result_str

    def list(self):
        image_and_objects = self.__index_access.get_all_images_and_objects()
        self.__output_formatter.set_strategy(AlphabeticalAscendingFormat())
        result_str = self.__output_formatter.format_data(image_and_objects)
        result_str += f"\n{len(image_and_objects)} images found."
        return result_str