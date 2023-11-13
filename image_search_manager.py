from num_descending_format import NumDescendingFormat
from alphabetical_ascending_format import AlphabeticalAscendingFormat
from cosine_similarity import CosineSimilarity


class ImageSearchManager:
    def __init__(self, output_formatter, object_detection, index_access, image_access, matching_engine):
        self.__output_formatter = output_formatter
        self.__object_detection = object_detection
        self.__index_access = index_access
        self.__image_access = image_access
        self.__matching_engine = matching_engine

    def add(self, image_path) -> str:
        detected_objects = self.__detect_and_store_objects(image_path)
        return self.__format_detected_objects(detected_objects)

    def search(self, option, terms) -> str:
        result_img_objects = self.__get_search_results(option, terms)
        self.__output_formatter.set_strategy(AlphabeticalAscendingFormat())
        return self.__format_search_results(result_img_objects)

    def similar(self, k, image_path):
        self.__output_formatter.set_strategy(NumDescendingFormat())
        self.__matching_engine.set_strategy(CosineSimilarity())

        encoded_objects, encoded_all_images_objects = self.__prepare_encoded_objects(image_path)
        matching_results = self.__matching_engine.execute_matching(encoded_objects, encoded_all_images_objects)
        return self.__format_matching_results(matching_results, k)

    def list(self):
        image_and_objects = self.__index_access.get_all_images_and_objects()
        self.__output_formatter.set_strategy(AlphabeticalAscendingFormat())
        return self.__format_search_results(image_and_objects)

    def __detect_and_store_objects(self, image_path):
        self.__index_access.add_image_path(image_path)
        image_data = self.__image_access.read_image(image_path)
        detected_objects = sorted(self.__object_detection.detect_objects(image_data))
        self.__index_access.add_detected_objects(image_path, detected_objects)
        return detected_objects

    def __format_detected_objects(self, detected_objects):
        return "Detected objects " + ",".join(detected_objects) + '\n'

    def __get_search_results(self, option, terms):
        return self.__index_access.get_images_with_all_objects(terms) if option else self.__index_access.get_images_with_some_objects(terms)

    def __format_search_results(self, results):
        formatted_results = self.__output_formatter.format_data(results)
        return formatted_results + f"\n{len(results)} matches found.\n"

    def __prepare_encoded_objects(self, image_path):
        all_images_objects = self.__index_access.get_all_images_and_objects()
        objects_detected = all_images_objects.get(image_path) or self.__object_detection.detect_objects(self.__image_access.read_image(image_path))
        encoded_objects = self.__object_detection.encode_labels(objects_detected)
        encoded_all_images_objects = {path: self.__object_detection.encode_labels(labels) for path, labels in all_images_objects.items()}
        return encoded_objects, encoded_all_images_objects

    def __format_matching_results(self, results, k):
        formatted_results = self.__output_formatter.format_data(results, k)
        return formatted_results + '\n'
