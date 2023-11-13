import numpy as np


class MatchingEngine:
    def __init__(self):
        self.__strategy = None

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def __calculate_similarity(self, flat_ndarray1, flat_ndarray2) -> float:
        return self.__strategy.calculate_similarity(flat_ndarray1, flat_ndarray2)
    
    def _reshape_image(self, image):
        image_array = np.array(image)
        return image_array.reshape(1, -1)

    def execute_matching(self, image1, encoded_objects_with_paths) -> dict:
        results = {}
        image1_reshaped = self._reshape_image(image1)

        for img_path, detected_objs in encoded_objects_with_paths.items():
            detected_objs_reshaped = self._reshape_image(detected_objs)
            similarity_score = self.__calculate_similarity(image1_reshaped, detected_objs_reshaped)
            results[img_path] = float(similarity_score)

        return results
