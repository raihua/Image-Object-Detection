import pytest
from src.alphabetical_ascending_format import AlphabeticalAscendingFormat


@pytest.fixture
def format_alphabet_asc():
    return AlphabeticalAscendingFormat()


@pytest.fixture
def image_data():
    image_data = (
        ("example_images/image3.jpg", ["person", "chair"]),
        ("example_images/image2.jpg", ["truck", "person", "car"]),
        ("example_images/image1.jpg", ["chair", "dining table", "potted plant"]),
    )

    return image_data


def test_format_data(format_alphabet_asc, image_data):
    result = format_alphabet_asc.format_data(image_data)
    
    expected_result = 'example_images/image1.jpg: chair,dining table,potted plant\nexample_images/image2.jpg: car,person,truck\nexample_images/image3.jpg: chair,person'

    assert result == expected_result
