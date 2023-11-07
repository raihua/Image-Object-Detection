import pytest
from .. import project_root
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

def test_search(manager):
    pass

def test_search_boundary(manager):
    pass

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