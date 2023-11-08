import pytest
from .. import project_root
from src.data_access.sqlite_indexing import SQLiteIndexing

@pytest.fixture
def sqlite_index():
    return SQLiteIndexing()

@pytest.fixture
def car_path():
    return "example_images/image4.jpg"

@pytest.fixture
def search_objects():
    return ["car", "person"]

def test_add_image_path(sqlite_index, path):
    sqlite_index.add_image_path(path)

def test_get_detected_objects(path,detected_objects):
    pass

def test_get_images_with_all_objects(sqlite_index, search_objects, car_path):
    image_path = sqlite_index.get_images_with_all_objects(search_objects)
    assert image_path == car_path

def test_get_images_with_any_objects(sqlite_index, search_objects, car_path):
    image_path = sqlite_index.get_images_with_any_objects(search_objects)
    assert image_path == car_path