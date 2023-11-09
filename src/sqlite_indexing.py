import sqlite3

from src.index_strategy import IndexStrategy
from src.sqlite_queries import (
    CREATE__IMAGES_TABLE_QUERY,
    CREATE_DETECTED_OBJECTS_TABLE_QUERY,
    INSERT_IMAGE_PATH_PARAM_QUERY,
    SELECT_INCLUDE_ALL_DETECTED,
    SELECT_INCLUDE_SOME_DETECTED,
    INSERT_DETECTED_OBJECTS_PARAM_QUERY,
)


class SQLiteIndexing(IndexStrategy):
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(CREATE__IMAGES_TABLE_QUERY)
        self.cursor.execute(CREATE_DETECTED_OBJECTS_TABLE_QUERY)
        self.conn.commit()

    def add_image_path(self, path):
        self.cursor.execute(INSERT_IMAGE_PATH_PARAM_QUERY, (path,))
        self.conn.commit()

    def add_detected_objects(self, image_path, objects):
        values = [(image_path, obj) for obj in objects]
        self.cursor.executemany(INSERT_DETECTED_OBJECTS_PARAM_QUERY, values)
        self.conn.commit()

    def get_images_with_all_objects(self, objects):
        query = SELECT_INCLUDE_ALL_DETECTED.format(
            ", ".join(["?"] * len(objects)), len(objects)
        )
        result = self.cursor.execute(query, objects).fetchall()
        return [row[0] for row in result]

    def get_images_with_some_objects(self, objects):
        query = SELECT_INCLUDE_SOME_DETECTED.format(", ".join(["?"] * len(objects)))
        result = self.cursor.execute(query, objects).fetchall()
        return [row[0] for row in result]
