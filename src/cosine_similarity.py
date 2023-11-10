from sklearn.metrics.pairwise import cosine_similarity
from similarity_strategy import SimilarityStrategy
from index_access import IndexAccess


class CosineSimilarity(SimilarityStrategy):
    def __init__(self):
        super().__init__()

    def calculate_similarity(self, image, image_compared):
        similarity = cosine_similarity(image, image_compared)
        return similarity