import pytest
from numpy import ndarray
from matplotlib.image import imread
from src.cosine_similarity import CosineSimilarity

def test_calculate_similarity():
    pic1 = imread("example_images/image1.jpg")
    results = CosineSimilarity.calculate_similarity(pic1, pic1)
    assert results == 1.0