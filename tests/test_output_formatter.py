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

    expected_result = (
        ("example_images/image1.jpg", 0.4082),
        ("example_images/image3.jpg", 1.0000),
        ("example_images/image6.jpg", 0.5000),
    )

    assert result == expected_result


def test_validate_k_no_exception(output_formatter, image_data):
    k = 3
    result = output_formatter.validate_k(k, image_data)
    assert result == k


def test_validate_k_less_than_2_exception(output_formatter, image_data):
    k = 1
    with pytest.raises(
        ValueError, match="k must be greater than or equal to 2 if provided"
    ):
        output_formatter.validate_k(k, image_data)


def test_get_top_k_results_alpha_acs(output_formatter, image_data):
    formatted_data = (
        ("example_images/image1.jpg", 0.4082),
        ("example_images/image2.jpg", 1.0000),
        ("example_images/image3.jpg", 1.0000),
    )

    k = 2
    result = output_formatter.get_top_k_results(formatted_data, k)

    expected_result = (
        ("example_images/image1.jpg", 0.4082),
        ("example_images/image2.jpg", 1.0000),
    )

    assert result == expected_result
