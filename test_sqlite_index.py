import pytest
import sqlite3
from sqlite_indexing import SQLiteIndexing


@pytest.fixture
def sqlite_indexing_connection_cursor():
    # Creating an in-memory SQLite database and executing table creation statements.
    sqlite_indexing = SQLiteIndexing()
    sqlite_indexing._SQLiteIndexing__conn = sqlite3.connect(":memory:")
    sqlite_indexing._SQLiteIndexing__create_table()
    conn = sqlite_indexing._SQLiteIndexing__conn
    cursor = sqlite_indexing._SQLiteIndexing__conn.cursor()
    yield sqlite_indexing, conn, cursor


@pytest.fixture
def insert_initial_data(sqlite_indexing_connection_cursor):
    _, conn, cursor = sqlite_indexing_connection_cursor
    # Insert image paths and associated objects in 'Detected_Objects' table
    image_path = "example_images/image1.jpg"
    cursor.execute(
        "INSERT INTO Images (image_path) VALUES (?);",
        (image_path,),  # Ensure the value is a tuple
    )
    cursor.execute(
        "INSERT INTO Detected_Objects (image_path, detected_object) VALUES (?, ?);",
        (image_path, "chair"),
    )
    cursor.execute(
        "INSERT INTO Detected_Objects (image_path, detected_object) VALUES (?, ?);",
        (image_path, "dining table"),
    )
    conn.commit()


def test_tables_exist(sqlite_indexing_connection_cursor):
    _, _, cursor = sqlite_indexing_connection_cursor

    # Check the existence of tables 'Images' and 'Detected_Objects'
    tables = ["Images", "Detected_Objects"]
    for table in tables:
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table,)
        )
        table_exists = cursor.fetchone() is not None
        assert table_exists


def test_add_image_path(sqlite_indexing_connection_cursor):
    sqlite_index, _, cursor = sqlite_indexing_connection_cursor

    image_path = "example_images/image1.jpg"
    sqlite_index.add_image_path(image_path)

    select_image_path_query = (
        "SELECT image_path FROM Images WHERE image_path = 'example_images/image1.jpg';"
    )
    cursor.execute(select_image_path_query)

    result = cursor.fetchone()
    assert result is not None


def test_add_detected_objects(sqlite_indexing_connection_cursor):
    sqlite_index, _, cursor = sqlite_indexing_connection_cursor

    detected_objects = ["car"]
    image_path = "example_images/image4.jpg"

    sqlite_index.add_detected_objects(image_path, detected_objects)

    # Complete the query to check for the detected objects at the image_path
    query = """
    SELECT * 
    FROM Detected_Objects 
    WHERE image_path = ? AND detected_object = ?;
    """

    cursor.execute(
        query, (image_path, detected_objects[0])
    )  # Assuming the first element is 'car'

    result = cursor.fetchone()
    assert result is not None


def test_get_images_with_all_objects(
    sqlite_indexing_connection_cursor, insert_initial_data
):
    sqlite_index, _, _ = sqlite_indexing_connection_cursor

    objects_to_find = ("chair", "dining table")
    result_image_and_path = sqlite_index.get_images_with_all_objects(objects_to_find)
    expected_image_and_paths = {"example_images/image1.jpg": ["chair", "dining table"]}
    assert result_image_and_path == expected_image_and_paths


def test_get_images_with_some_objects(
    sqlite_indexing_connection_cursor, insert_initial_data
):
    sqlite_index, _, _ = sqlite_indexing_connection_cursor

    objects_to_find = ("potted plant", "dining table")
    result_image_and_path = sqlite_index.get_images_with_some_objects(objects_to_find)
    expected_image_and_paths = {"example_images/image1.jpg": ["chair", "dining table"]}
    assert result_image_and_path == expected_image_and_paths


def test_get_all_images_and_objects(
    sqlite_indexing_connection_cursor, insert_initial_data
):
    sqlite_index, _, _ = sqlite_indexing_connection_cursor

    results = sqlite_index.get_all_images_and_objects()
    example_result = {"example_images/image1.jpg": ["chair", "dining table"]}
    assert results == example_result