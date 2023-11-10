import sklearn.metrics.pairwise as smp
from similarity_strategy import SimilarityStrategy


class CosineSimilarity(SimilarityStrategy):
    def __init__(self):
        super().__init__()

    def calculate_similarity(self, image, image_compared):
        similarity = smp.cosine_similarity(image, image_compared)
        return similarity
