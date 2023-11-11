import numpy as np


class MatchingEngine:
    def __init__(self):
        self.__strategy = None

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def __calculate_similarity(self, flat_ndarray1, flat_ndarray2) -> float:
        return self.__strategy.calculate_similarity(flat_ndarray1, flat_ndarray2)

    def execute_matching(self, image1, encoded_objects_with_paths) -> tuple:
        results = []
        for img_path, detected_objs in encoded_objects_with_paths:
            # TODO might not need flatten if we have encode from object detection.
            similarity_score = self.__calculate_similarity(image1, detected_objs)
            results.append((img_path, similarity_score))

        return tuple(results)
