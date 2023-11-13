import pytest
from unittest.mock import Mock, create_autospec, patch, call
import sqlite3
from sqlite_indexing import SQLiteIndexing
from sqlite_queries import (
    CREATE__IMAGES_TABLE_QUERY,
    CREATE_DETECTED_OBJECTS_TABLE_QUERY,
    INSERT_IMAGE_PATH_PARAM_QUERY,
    SELECT_INCLUDE_ALL_DETECTED,
    SELECT_INCLUDE_SOME_DETECTED,
    INSERT_DETECTED_OBJECTS_PARAM_QUERY,
    SELECT_ALL_IMAGES_OBJECTS_QUERY,
    SELECT_COUNT_PATH,
    SELECT_COUNT_DETECTED,
)
# Mocking the sqlite3 connection
@pytest.fixture
def mock_sqlite3(monkeypatch):
    mock_conn = create_autospec(sqlite3.Connection, instance=True)
    mock_cursor = create_autospec(sqlite3.Cursor, instance=True)
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('sqlite3.connect', Mock(return_value=mock_conn))
    return mock_conn, mock_cursor

# Tests for SQLiteIndexing
def test_create_table(mock_sqlite3):
    mock_conn, mock_cursor = mock_sqlite3
    indexing = SQLiteIndexing()
    indexing._SQLiteIndexing__conn = mock_conn

    mock_cursor.execute.assert_has_calls([
        call(CREATE__IMAGES_TABLE_QUERY),
        call(CREATE_DETECTED_OBJECTS_TABLE_QUERY)
    ])
    mock_conn.commit.assert_called_once()

def test_add_image_path(mock_sqlite3):
    mock_conn, mock_cursor = mock_sqlite3
    mock_cursor.fetchone.return_value = [0]  # Simulating path not existing

    indexing = SQLiteIndexing()
    indexing.add_image_path('test.jpg')

    mock_cursor.execute.assert_called_with(INSERT_IMAGE_PATH_PARAM_QUERY, ('test.jpg',))
    mock_conn.commit.assert_called_once()

def test_add_detected_objects(mock_sqlite3):
    mock_conn, mock_cursor = mock_sqlite3
    mock_cursor.fetchone.return_value = [0]  # Simulating object not existing

    indexing = SQLiteIndexing()
    indexing.add_detected_objects('test.jpg', ['object1', 'object2'])

    expected_calls = [
        call(INSERT_DETECTED_OBJECTS_PARAM_QUERY, ('test.jpg', 'object1')),
        call(INSERT_DETECTED_OBJECTS_PARAM_QUERY, ('test.jpg', 'object2'))
    ]
    mock_cursor.execute.assert_has_calls(expected_calls)
    assert mock_conn.commit.call_count == len(['object1', 'object2'])

# Additional tests can be written for get_images_with_all_objects, get_images_with_some_objects, and get_all_images_and_objects
