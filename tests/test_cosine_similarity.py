import pytest
import numpy as np
from matplotlib.image import imread
from src.cosine_similarity import CosineSimilarity


@pytest.fixture
def cosine_similarity():
    return CosineSimilarity()


def test_calculate_similarity(cosine_similarity):
    original_array = np.array([[1, 2], [3, 4]])
    flattened_array = original_array.flatten().reshape(1, -1)
    result = cosine_similarity.calculate_similarity(flattened_array, flattened_array)
    assert result == pytest.approx(1)
