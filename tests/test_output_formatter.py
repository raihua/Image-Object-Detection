import pytest
from src.output_formatter import OutputFormatter
from src.alphabetical_ascending_format import AlphabeticalAscendingFormat
from src.num_descending_format import NumDescendingFormat


@pytest.fixture
def alpha_asc_format():
    return AlphabeticalAscendingFormat()


@pytest.fixture
def num_desc_format():
    return NumDescendingFormat()


@pytest.fixture
def output_formatter(alpha_asc_format):
    strategy = alpha_asc_format
    yield OutputFormatter(strategy)


@pytest.fixture
def image_data():
    image_data = {
        "example_images/image3.jpg": 1.0000,
        "example_images/image6.jpg": 0.5000,
        "example_images/image1.jpg": 0.4082,
    }

    return image_data


def test_set_strategy(output_formatter, num_desc_format):
    output_formatter.set_strategy(num_desc_format)
    assert isinstance(output_formatter._OutputFormatter__strategy, NumDescendingFormat)


def test_format_data(output_formatter, image_data):
    result = output_formatter.format_data(image_data)

    expected_result = {
        "example_images/image1.jpg": 0.4082,
        "example_images/image3.jpg": 1.0000,
        "example_images/image6.jpg": 0.5000,
    }

    assert result == expected_result
