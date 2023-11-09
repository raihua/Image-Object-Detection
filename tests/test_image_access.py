import pytest
from numpy import ndarray
from src.image_access import ImageAccess

def test_read_image():
    image_access = ImageAccess("example_images")
    result = image_access.read_image("image1.jpg")
    assert isinstance(result, ndarray)
