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


def test_search_some(image_search_manager):
    search_terms = ("car", "person")
    expected_result = """example_images/image2.jpg: car,person,truck\nexample_images/image3.jpg: chair,person\nexample_images/image4.jpg: car\nexample_images/image5.jpg: car,person,traffic light\n4 matches found."""
    result = image_search_manager.search(False, search_terms)
    assert result == expected_result

# def test_similar_k_999(image_search_manager, insert_6_images):
#     k = 999
#     image_path = "example_images/image3.jpg"
#     result = image_search_manager.similar(k, image_path)
#     expected_result = """
#     1.0000 example_images/image3.jpg\n
#     0.5000 example_images/image6.jpg\n
#     0.4082 example_images/image1.jpg\n
#     0.4082 example_images/image2.jpg\n
#     0.4082 example_images/image5.jpg\n
#     0.0000 example_images/image4.jpg\n
#     """
#     assert result == expected_result

# def test_similar_k_3(image_search_manager, insert_6_images):
#     k = 3
#     image_path = "example_images/image3.jpg"
#     result = image_search_manager.similar(k, image_path)
#     expected_result = """
#     1.0000 example_images/image3.jpg\n
#     0.5000 example_images/image6.jpg\n
#     0.4082 example_images/image1.jpg\n
#     """
#     assert result == expected_result

# def test_list(image_search_manager, insert_6_images):
#     result = image_search_manager.list()
#     expected_result = """
#     example_images/image1.jpg: chair,dining table,potted plant\n
#     example_images/image2.jpg: car,person,truck\n
#     example_images/image3.jpg: chair,person\n
#     example_images/image4.jpg: car\n
#     example_images/image5.jpg: car,person,traffic light\n
#     example_images/image6.jpg: chair,couch\n
#     6 images found.\n
#     """
#     assert result == expected_result
