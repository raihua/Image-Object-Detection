import pytest
from src.num_descending_format import NumDescendingFormat


@pytest.fixture
def format_num_descending():
    return NumDescendingFormat()


@pytest.fixture
def image_data():
    image_data = (
        ("example_images/image3.jpg", 1.0000),
        ("example_images/image6.jpg", 0.5000),
        ("example_images/image1.jpg", 0.4082),
    )


    return image_data


def test_format_data(format_num_descending, image_data):
    result = format_num_descending.format_data(image_data)

    expected_result = (
        ("example_images/image3.jpg", 1.0000),
        ("example_images/image6.jpg", 0.5000),
        ("example_images/image1.jpg", 0.4082),
    )

    assert result == expected_result
