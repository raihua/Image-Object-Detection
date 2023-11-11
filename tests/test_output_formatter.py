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
def output_formatter(num_desc_format):
    strategy = num_desc_format
    output_formatter = OutputFormatter()
    output_formatter.set_strategy(strategy)
    yield output_formatter


@pytest.fixture
def float_image_data():
    float_image_data = (
        ("example_images/image3.jpg", 1.0000),
        ("example_images/image6.jpg", 0.5000),
        ("example_images/image1.jpg", 0.4082),
    )

    return float_image_data


@pytest.fixture
def str_image_data():
    str_image_data = (
        ("example_images/image3.jpg", ["person", "chair"]),
        ("example_images/image2.jpg", ["truck", "person", "car"]),
        ("example_images/image1.jpg", ["chair", "dining table", "potted plant"]),
    )

    return str_image_data


def test_set_strategy(output_formatter, num_desc_format):
    output_formatter.set_strategy(num_desc_format)
    assert isinstance(output_formatter._OutputFormatter__strategy, NumDescendingFormat)


def test_format_data(output_formatter, str_image_data, alpha_asc_format):
    output_formatter.set_strategy(alpha_asc_format)
    result = output_formatter.format_data(str_image_data)

    expected_result = (
        ("example_images/image1.jpg", ["chair", "dining table", "potted plant"]),
        ("example_images/image2.jpg", ["car", "person", "truck"]),
        ("example_images/image3.jpg", ["chair", "person"]),
    )

    assert result == expected_result


def test_validate_k_no_exception(output_formatter, float_image_data):
    k = 3
    result = output_formatter._OutputFormatter__validate_k(k, float_image_data)
    assert result == k


def test_validate_k_less_than_2_exception(output_formatter, float_image_data):
    k = 1
    with pytest.raises(
        ValueError, match="k must be greater than or equal to 2 if provided"
    ):
        output_formatter._OutputFormatter__validate_k(k, float_image_data)


def test_get_top_k_results_alpha_acs(output_formatter, float_image_data):
    formatted_data = (
        ("example_images/image1.jpg", 0.4082),
        ("example_images/image2.jpg", 1.0000),
        ("example_images/image3.jpg", 1.0000),
    )

    k = 2
    result = output_formatter._OutputFormatter__get_top_k_results(formatted_data, k)

    expected_result = (
        ("example_images/image1.jpg", 0.4082),
        ("example_images/image2.jpg", 1.0000),
    )

    assert result == expected_result
