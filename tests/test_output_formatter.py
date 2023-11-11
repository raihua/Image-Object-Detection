import pytest
from src.output_formatter import OutputFormatter
from src.alphabetical_ascending_format import AlphabeticalAscendingFormat
from src.num_descending_format import NumDescendingFormat


@pytest.fixture
def alpha_asc_format():
    asc_format = AlphabeticalAscendingFormat()
    yield asc_format


@pytest.fixture
def num_desc_format():
    num_desc_format = NumDescendingFormat()
    yield num_desc_format


@pytest.fixture
def output_formatter():
    output_formatter = OutputFormatter()
    yield output_formatter


@pytest.fixture
def float_image_data():
    float_image_data = {
        "example_images/image3.jpg": 1.0000,
        "example_images/image6.jpg": 0.5000,
        "example_images/image1.jpg": 0.4082,
    }
    return float_image_data


@pytest.fixture
def str_image_data():
    str_image_data = {
        "example_images/image3.jpg": ["person", "chair"],
        "example_images/image2.jpg": ["truck", "person", "car"],
        "example_images/image1.jpg": ["chair", "dining table", "potted plant"],
    }

    return str_image_data


def test_set_strategy(output_formatter, alpha_asc_format):
    output_formatter.set_strategy(alpha_asc_format)
    assert isinstance(output_formatter._OutputFormatter__strategy, AlphabeticalAscendingFormat)


def test_format_data(output_formatter, str_image_data, alpha_asc_format):
    output_formatter.set_strategy(alpha_asc_format)
    result = output_formatter.format_data(str_image_data)

    expected_result = """example_images/image1.jpg: chair,dining table,potted plant
example_images/image2.jpg: car,person,truck
example_images/image3.jpg: chair,person"""

    assert result == expected_result

def test_get_top_k_results(output_formatter, str_image_data):
    k = 2

    expected_result = {
        "example_images/image3.jpg": ["person", "chair"],
        "example_images/image2.jpg": ["truck", "person", "car"],
    }

    result = output_formatter._OutputFormatter__get_top_k_results(str_image_data, 2)

    assert result == expected_result

