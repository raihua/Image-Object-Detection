from abc import ABC, abstractmethod


class SimilarityStrategy:
    @abstractmethod
    def calculate_similarity(self, image1, images):
        pass
