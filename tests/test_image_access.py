import pytest
from numpy import ndarray
from src.image_access import ImageAccess

def test_read_image():
    image_access = ImageAccess("example_images/image1.jpg")
    result = image_access.read_image()
    assert isinstance(result, ndarray)
