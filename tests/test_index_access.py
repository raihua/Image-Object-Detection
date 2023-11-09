import pytest
from src.index_access import IndexAccess
from src.sqlite_indexing import SQLiteIndexing


@pytest.fixture
def index_access():
    strategy = SQLiteIndexing(":memory:")
    index_access = IndexAccess(strategy)
    yield index_access

@pytest.fixture
def sqlite_cursor(index_access):
    yield index_access.strategy.cursor

@pytest.fixture
def insert_initial_data(index_access):
    # Insert image paths and associated objects in 'Detected_Objects' table
    image_path = "example_images/image1.jpg"
    index_access.add_image_path(image_path)
    index_access.add_detected_objects(image_path, ["chair", "dining table"])

def test_get_strategy(index_access):
    assert isinstance(index_access.strategy, SQLiteIndexing)


def test_set_strategy(index_access):
    new_strategy = None
    index_access.strategy = new_strategy
    assert index_access.strategy == new_strategy


def test_add_image_path(index_access, sqlite_cursor):
    image_path = "example_images/image1.jpg"
    index_access.add_image_path(image_path)
    sqlite_cursor.execute(f"SELECT image_path from Images where image_path = ?", (image_path,))
    result = sqlite_cursor.fetchone()
    assert result[0] == image_path


def test_add_detected_objects(index_access, sqlite_cursor):
    image_path = "example_images/image4.jpg"
    detected_object = "car"
    index_access.add_detected_objects(image_path, detected_object)
    # Complete the query to check for the detected objects at the image_path
    query = """
    SELECT detected_object 
    FROM Detected_Objects 
    WHERE image_path = ? AND detected_object = ?;
    """
    sqlite_cursor.execute(
        query, (image_path, detected_object)
    )  # Assuming the first element is 'car'

    result = sqlite_cursor.fetchone()
    assert result[0] == detected_object
    

def test_get_images_with_all_objects(index_access, sqlite_cursor, insert_initial_data):
    objects_to_find = ["chair", "dining table"]
    result_paths = index_access.get_images_with_all_objects(objects_to_find)
    expected_image_paths = ["example_images/image1.jpg"]
    assert result_paths == expected_image_paths


def test_get_images_with_some_objects(index_access, sqlite_cursor, insert_initial_data):
    objects_to_find = ["potted plant", "dining table"]
    result_paths = index_access.get_images_with_some_objects(objects_to_find)
    expected_image_paths = ["example_images/image1.jpg"]
    assert result_paths == expected_image_paths


