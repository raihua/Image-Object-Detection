from src.num_descending_format import NumDescendingFormat
from src.alphabetical_ascending_format import AlphabeticalAscendingFormat
from src.cosine_similarity import CosineSimilarity


class ImageSearchManager:
    def __init__(self, output_formatter, object_detection, index_access, image_access, matching_engine):
        self.__output_formatter = output_formatter
        self.__object_detection = object_detection
        self.__index_access = index_access
        self.__image_access = image_access
        self.__matching_engine = matching_engine

    def add(self, image_path) -> str:
        self.__index_access.add_image_path(image_path)
        image_data = self.__image_access.read_image(image_path)
        detected_objects = sorted(
            self.__object_detection.detect_objects(image_data))
        self.__index_access.add_detected_objects(image_path, detected_objects)
        result_str = "Detected objects " + ",".join(detected_objects) + '\n'
        return result_str

    def search(self, option, terms) -> str:
        result_img_objects = None
        if option:
            result_img_objects = self.__index_access.get_images_with_all_objects(
                terms)
        else:
            result_img_objects = self.__index_access.get_images_with_some_objects(
                terms)

        self.__output_formatter.set_strategy(AlphabeticalAscendingFormat())
        result_str = self.__output_formatter.format_data(result_img_objects)
        result_str += f"\n{len(result_img_objects)} matches found.\n"
        return result_str

    def similar(self, k, image_path):
        self.__output_formatter.set_strategy(NumDescendingFormat())
        self.__matching_engine.set_strategy(CosineSimilarity())

        all_images_objects = self.__index_access.get_all_images_and_objects()

        objects_detected = None
        if image_path not in all_images_objects.keys():
            image_data = self.__image_access.read_image(image_path)
            objects_detected = self.__object_detection.detect_objects(
                image_data)
        else:
            objects_detected = all_images_objects[image_path]

        encoded_objects = self.__object_detection.encode_labels(
            objects_detected)

        encoded_all_images_objects = {}
        for path, labels in all_images_objects.items():
            encoded_labels = self.__object_detection.encode_labels(labels)
            encoded_all_images_objects[path] = encoded_labels

        matching_results = self.__matching_engine.execute_matching(
            encoded_objects, encoded_all_images_objects
        )

        result_str = self.__output_formatter.format_data(matching_results, k)
        return result_str + '\n'

    def list(self):
        image_and_objects = self.__index_access.get_all_images_and_objects()
        self.__output_formatter.set_strategy(AlphabeticalAscendingFormat())
        result_str = self.__output_formatter.format_data(image_and_objects)
        result_str += f"\n{len(image_and_objects)} images found.\n"
        return result_str
