import pytest
import numpy as np
from src.image_access import ImageAccess


@pytest.fixture
def image_access():
    return ImageAccess()


def test_read_image(image_access):
    result = image_access.read_image("example_images/image1.jpg")
    assert isinstance(result, np.ndarray)

