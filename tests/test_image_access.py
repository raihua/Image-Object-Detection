import pytest
import numpy as np
from src.image_access import ImageAccess


@pytest.fixture
def image_access():
    return ImageAccess()


def test_read_image(image_access):
    result = image_access.read_image("example_images/image1.jpg")
    assert isinstance(result, np.ndarray)


def test_flatten_and_reshape_image(image_access):
    vector = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    ]
    numpy_array = np.array(vector)

    flat_vector = image_access.flatten_and_reshape_image(numpy_array)

    expected_vector = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]

    assert np.array_equal(flat_vector, expected_vector)
