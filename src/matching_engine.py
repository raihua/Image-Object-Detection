import numpy as np


class MatchingEngine:
    def __init__(self, strategy):
        self.__strategy = strategy

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def calculate_similarity(self, flat_ndarray1, flat_ndarray2):
        return self.__strategy.calculate_similarity(flat_ndarray1, flat_ndarray2)

    def execute_matching(self, image1, images_dict):
        results = {}
        for img_path, detected_objs in images_dict.items():
            # TODO might not need flatten if we have encode from object detection.
            image2_vector = np.array(detected_objs).flatten().reshape(1, -1)
            similarity_score = self.calculate_similarity(image1, image2_vector)
            results[img_path] = similarity_score

        return results
