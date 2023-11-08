import pytest
import sqlite3
from src.sqlite_indexing import SQLiteIndexing

@pytest.fixture
def sqlite_memory_db():
    sqlite_memory_db = SQLiteIndexing(":memory:")
    return sqlite_memory_db

def test_sqlite_connection(sqlite_memory_db):
    sqlite_conn = sqlite_memory_db.conn
    assert isinstance(sqlite_conn, sqlite3.Connection)

