from sklearn.metrics.pairwise import cosine_similarity
from simalarity_strategy import SimalarityStrategy
from index_access import IndexAccess

class CosineSimalarity(SimalarityStrategy):
    def __init__(self):
        super().__init__()

    def calculate_simalarity(self, image, images_dict):
        return cosine_similarity(image,images_dict)