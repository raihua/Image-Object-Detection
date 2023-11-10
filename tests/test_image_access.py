import pytest
import numpy as np
from src.image_access import ImageAccess

@pytest.fixture
def image_access():
    return ImageAccess("example_images/image1.jpg")


def test_read_image(image_access):
    result = image_access.read_image()
    assert isinstance(result, np.ndarray)

def test_flatten_and_reshape_image(image_access):
    # Test input: 2x3 image
    image_data = np.array([[1, 2, 3],
                           [4, 5, 6]])

    # Expected output: Flattened and reshaped to a 1D array
    expected_result = np.array([1, 2, 3, 4, 5, 6]).reshape(1, -1)

    # Call the function
    result = image_access.flatten_and_reshape_image(image_data)

    # Assertion
    assert np.array_equal(result, expected_result)