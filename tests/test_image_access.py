import pytest
import numpy as np
from src.image_access import ImageAccess


@pytest.fixture
def image_access():
    return ImageAccess()


def test_read_image(image_access):
    result = image_access.read_image("example_images/image1.jpg")
    assert isinstance(result, np.ndarray)


def test_validate_directory(image_access):
    with pytest.raises((ValueError, FileNotFoundError)):
        image_access.read_image("imcryingoutloud/images1.jpg")
