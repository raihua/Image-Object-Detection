import pytest
import sqlite3
from src.sqlite_indexing import SQLiteIndexing
from src.sqlite_queries import CREATE__IMAGES_TABLE_QUERY, CREATE_DETECTED_OBJECTS_TABLE_QUERY

@pytest.fixture
def sqlite_connection():
    # Creating in memory sqlite db and execute table creation statements.
    sqlite_connection = SQLiteIndexing(":memory:")
    sqlite_connection.create_table()
    yield sqlite_connection
    sqlite_connection.close()


def test_sqlite_connection(sqlite_connection):
    sqlite_conn = sqlite_connection.conn
    assert isinstance(sqlite_conn, sqlite3.Connection)


def test_tables_exist(sqlite_connection):
    sqlite_connection.create_table()
    
    # Check for 'Images' table
    sqlite_connection.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", ("Images",))
    image_table_exists = sqlite_connection.cursor.fetchone() is not None

    # Check for 'Detected_Objects' table
    sqlite_connection.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", ("Detected_Objects",))
    detected_table_exists = sqlite_connection.cursor.fetchone() is not None

    assert image_table_exists and detected_table_exists


def test_add_image_path(sqlite_connection):
    image_path = "example_images/image1.jpg"
    select_image_path_query = "SELECT image_path FROM Images WHERE image_path = 'example_images/image1.jpg';"
    sqlite_connection.add_image_path(image_path)
    sqlite_connection.cursor.execute(select_image_path_query)
    result = sqlite_connection.cursor.fetchone()
    assert result is not None
