import sklearn.metrics.pairwise as smp
from similarity_strategy import SimilarityStrategy


class CosineSimilarity(SimilarityStrategy):
    def __init__(self):
        super().__init__()

    def calculate_similarity(self, image, image_compared) -> float:
        similarity = smp.cosine_similarity(image, image_compared)
        float_similarity = similarity[0, 0]
        return float_similarity
