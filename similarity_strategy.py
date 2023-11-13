from abc import ABC, abstractmethod


class SimilarityStrategy(ABC):
    @abstractmethod
    def calculate_similarity(self, image1, images) -> float:
        pass
