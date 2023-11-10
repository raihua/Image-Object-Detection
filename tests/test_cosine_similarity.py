import pytest
import numpy as np
from matplotlib.image import imread
from src.cosine_similarity import CosineSimilarity

@pytest.fixture
def cosine_similarity():
    return CosineSimilarity()

def test_calculate_similarity(cosine_similarity):
    # Load the image
    image_path = "example_images/image1.jpg"
    image = imread(image_path)

    # Flatten and reshape the image for similarity calculation
    flat_image = image.flatten().reshape(1, -1)

    # Create an instance of CosineSimilarity
    cosine_similarity = CosineSimilarity()

    # Call the calculate_similarity method with the image for comparison
    result = cosine_similarity.calculate_similarity(flat_image, flat_image)

    # Assert that the similarity is close to 1.0
    assert np.isclose(result, 1.0, atol=1e-10), f"Expected similarity close to 1.0, got {result}"