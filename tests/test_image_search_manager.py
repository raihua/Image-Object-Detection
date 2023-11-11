import pytest
from src.image_search_manager import ImageSearchManager


@pytest.fixture
def image_search_manager():
    return ImageSearchManager()


@pytest.fixture
def insert_6_images(image_search_manager):
    image_search_manager.add("example_images/image3.jpg")
    image_search_manager.add("example_images/image6.jpg")
    image_search_manager.add("example_images/image1.jpg")
    image_search_manager.add("example_images/image2.jpg")
    image_search_manager.add("example_images/image5.jpg")
    image_search_manager.add("example_images/image4.jpg")


def test_injest_image(image_search_manager):
    file_path = "example_images/image1.jpg"
    result = image_search_manager.add(file_path)
    expected_result = "Detected objects chair,dining table,potted plant"
    assert result == expected_result


def test_search_all(image_search_manager, insert_6_images):
    search_terms = ("car", "person")
    expected_result = """example_images/image2.jpg: car,person,truck\nexample_images/image5.jpg: car,person,traffic light\n2 matches found."""
    result = image_search_manager.search(True, search_terms)
    assert result.strip() == expected_result.strip()


def test_search_some(image_search_manager, insert_6_images):
    search_terms = ("car", "person")
    expected_result = """example_images/image2.jpg: car,person,truck\nexample_images/image3.jpg: chair,person\nexample_images/image4.jpg: car\nexample_images/image5.jpg: car,person,traffic light\n4 matches found."""
    result = image_search_manager.search(False, search_terms)
    assert result == expected_result


def test_similar_k_999(image_search_manager, insert_6_images):
    k = 999
    image_path = "example_images/image3.jpg"
    result = image_search_manager.similar(k, image_path)
    expected_result = """
    1.0000 example_images/image3.jpg
    0.5000 example_images/image6.jpg
    0.4082 example_images/image1.jpg
    0.4082 example_images/image2.jpg
    0.4082 example_images/image5.jpg
    0.0000 example_images/image4.jpg
    """

    # Split the expected and actual results into lines
    expected_lines = expected_result.strip().split("\n")
    actual_lines = result.strip().split("\n")

    # Check if the number of lines matches
    assert len(expected_lines) == len(actual_lines)

    # Iterate over corresponding lines and compare numeric values with tolerance
    for expected_line, actual_line in zip(expected_lines, actual_lines):
        expected_parts = expected_line.split()
        actual_parts = actual_line.split()

        # Check if there are enough elements in the line
        if len(expected_parts) < 2 or len(actual_parts) < 2:
            raise AssertionError("Invalid line format")

        expected_value = float(expected_parts[0])
        actual_value = float(actual_parts[0])

        # Define a tolerance (adjust as needed)
        tolerance = 1e-4

        assert abs(expected_value - actual_value) <= tolerance


def test_list(image_search_manager, insert_6_images):
    result = image_search_manager.list()
    expected_result = """
example_images/image1.jpg: chair,dining table,potted plant
example_images/image2.jpg: car,person,truck
example_images/image3.jpg: chair,person
example_images/image4.jpg: car
example_images/image5.jpg: car,person,traffic light
example_images/image6.jpg: chair,couch
6 images found.
"""
    assert result.strip() == expected_result.strip()

