import pytest
import sqlite3
from src.index_access import IndexAccess
from src.sqlite_indexing import SQLiteIndexing


@pytest.fixture
def index_access_sqlite_index_cursor():
    conn = sqlite3.connect(":memory:")
    sqlite_indexing = SQLiteIndexing(conn)
    # Creating an in-memory SQLite database and executing table creation statements.
    index_access = IndexAccess(sqlite_indexing)
    cursor = conn.cursor()

    yield index_access, sqlite_indexing, cursor


@pytest.fixture
def insert_initial_data(index_access_sqlite_index_cursor):
    index_access, sqlite_indexing, _ = index_access_sqlite_index_cursor

    # Insert image paths and associated objects in 'Detected_Objects' table
    image_path = "example_images/image1.jpg"
    index_access.add_image_path(image_path)
    index_access.add_detected_objects(image_path, ["chair", "dining table"])


def test_set_strategy(index_access_sqlite_index_cursor):
    index_access, sqlite_indexing, cursor = index_access_sqlite_index_cursor
    index_access.set_strategy(sqlite_indexing)

    strategy = index_access._IndexAccess__strategy
    assert isinstance(strategy, SQLiteIndexing)


def test_add_image_path(index_access_sqlite_index_cursor):
    index_access, sqlite_indexing, cursor = index_access_sqlite_index_cursor
    image_path = "example_images/image1.jpg"
    index_access.add_image_path(image_path)
    cursor.execute(f"SELECT image_path from Images where image_path = ?", (image_path,))
    result = cursor.fetchone()
    assert result[0] == image_path


def test_add_detected_objects(index_access_sqlite_index_cursor):
    index_access, sqlite_indexing, cursor = index_access_sqlite_index_cursor
    image_path = "example_images/image4.jpg"
    detected_object = "car"
    index_access.add_detected_objects(image_path, detected_object)
    # Complete the query to check for the detected objects at the image_path
    query = """
    SELECT detected_object 
    FROM Detected_Objects 
    WHERE image_path = ? AND detected_object = ?;
    """
    cursor.execute(
        query, (image_path, detected_object)
    )  # Assuming the first element is 'car'

    result = cursor.fetchone()
    assert result[0] == detected_object


def test_get_images_with_all_objects(
    index_access_sqlite_index_cursor, insert_initial_data
):
    index_access, sqlite_indexing, cursor = index_access_sqlite_index_cursor

    objects_to_find = ["chair", "dining table"]
    result_paths = index_access.get_images_with_all_objects(objects_to_find)
    expected_image_paths = ["example_images/image1.jpg"]
    assert result_paths == expected_image_paths


def test_get_images_with_some_objects(
    index_access_sqlite_index_cursor, insert_initial_data
):
    index_access, sqlite_indexing, cursor = index_access_sqlite_index_cursor

    objects_to_find = ["potted plant", "dining table"]
    result_paths = index_access.get_images_with_some_objects(objects_to_find)
    expected_image_paths = ["example_images/image1.jpg"]
    assert result_paths == expected_image_paths
