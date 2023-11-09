import pytest
import sqlite3
from src.sqlite_indexing import SQLiteIndexing
from src.sqlite_queries import (
    CREATE__IMAGES_TABLE_QUERY,
    CREATE_DETECTED_OBJECTS_TABLE_QUERY,
)


@pytest.fixture
def sqlite_connection():
    # Creating in memory sqlite db and execute table creation statements.
    sqlite_connection = SQLiteIndexing(":memory:")
    sqlite_connection.create_table()
    yield sqlite_connection


@pytest.fixture
def insert_initial_data(sqlite_connection):
    # Insert image paths and associated objects in 'Detected_Objects' table
    image_path = "example_images/image1.jpg"
    sqlite_connection.cursor.execute(
        "INSERT INTO Detected_Objects (image_path, detected_object) VALUES (?, ?);",
        (image_path, "chair"),
    )
    sqlite_connection.cursor.execute(
        "INSERT INTO Detected_Objects (image_path, detected_object) VALUES (?, ?);",
        (image_path, "dining table"),
    )
    sqlite_connection.conn.commit()


def test_sqlite_connection(sqlite_connection):
    sqlite_conn = sqlite_connection.conn
    assert isinstance(sqlite_conn, sqlite3.Connection)


def test_tables_exist(sqlite_connection):
    # Check the existence of tables 'Images' and 'Detected_Objects'
    tables = ["Images", "Detected_Objects"]
    for table in tables:
        sqlite_connection.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table,)
        )
        table_exists = sqlite_connection.cursor.fetchone() is not None
        assert table_exists


def test_add_image_path(sqlite_connection):
    image_path = "example_images/image1.jpg"
    sqlite_connection.add_image_path(image_path)

    select_image_path_query = (
        "SELECT image_path FROM Images WHERE image_path = 'example_images/image1.jpg';"
    )
    sqlite_connection.cursor.execute(select_image_path_query)

    result = sqlite_connection.cursor.fetchone()
    assert result is not None


def test_add_detected_objects(sqlite_connection):
    detected_objects = ["car"]
    image_path = "example_images/image4.jpg"

    sqlite_connection.add_detected_objects(image_path, detected_objects)

    # Complete the query to check for the detected objects at the image_path
    query = """
    SELECT * 
    FROM Detected_Objects 
    WHERE image_path = ? AND detected_object = ?;
    """

    sqlite_connection.cursor.execute(
        query, (image_path, detected_objects[0])
    )  # Assuming the first element is 'car'

    result = sqlite_connection.cursor.fetchone()
    assert result is not None


def test_get_images_with_all_objects(sqlite_connection, insert_initial_data):
    objects_to_find = ["chair", "dining table"]
    result_paths = sqlite_connection.get_images_with_all_objects(objects_to_find)
    expected_image_paths = ["example_images/image1.jpg"]
    assert result_paths == expected_image_paths


def test_get_images_with_some_objects(sqlite_connection, insert_initial_data):
    objects_to_find = ["potted plant", "dining table"]
    result_paths = sqlite_connection.get_images_with_some_objects(objects_to_find)
    expected_image_paths = ["example_images/image1.jpg"]
    assert result_paths == expected_image_paths
