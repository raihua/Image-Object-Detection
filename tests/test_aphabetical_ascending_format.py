import pytest
from src.alphabetical_ascending_format import AlphabeticalAscendingFormat


@pytest.fixture
def format_alphabet_asc():
    return AlphabeticalAscendingFormat()


@pytest.fixture
def image_data():
    image_data = (
        ("example_images/image3.jpg", 1.0000),
        ("example_images/image6.jpg", 0.5000),
        ("example_images/image1.jpg", 0.4082),
    )

    return image_data


def test_format_data(format_alphabet_asc, image_data):
    result = format_alphabet_asc.format_data(image_data)
    
    expected_result = (
        ("example_images/image1.jpg", 0.4082),
        ("example_images/image3.jpg", 1.0000),
        ("example_images/image6.jpg", 0.5000),
    )

    assert result == expected_result
