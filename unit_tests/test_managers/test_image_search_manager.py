import pytest
from src.managers.image_search_manager import ImageSearchManager

@pytest.fixture
def manager():  
    return ImageSearchManager()

def test_add(manager):
    manager.add("example_images/image4.jpg")

def test_add_boundary(manager):
    with pytest.raises(TypeError):
        manager.add(5)
        manager.add(5.0)
        manager.add()

@pytest.fixture
def UC2_terms():
    return ["car", "person"]

def test_search_all(manager, UC2_terms):
    results = manager.search(True, UC2_terms)
    expected_results = [
        "example_images/image2.jpg: car,person,truck",
        "example_images/image5.jpg: car,person,traffic light"
    ]
    assert results == expected_results

def test_search_some(manager, UC2_terms):
    results = manager.search(False, UC2_terms)
    expected_results = [
        "example_images/image2.jpg: car,person,truck",
        "example_images/image3.jpg: chair,person",
        "example_images/image4.jpg: car",
        "example_images/image5.jpg: car,person,traffic light"
    ]
    assert results == expected_results

def test_similar(manager):
    pass

def test_similar_boundary(manager):
    pass

def test_list(manager):
    pass

def test_list_boundary(manager):
    pass

def test_set_model(manager):
    pass

def test_output_format(manager):
    pass