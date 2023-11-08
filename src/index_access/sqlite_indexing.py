import sqlite3
from .indexing_strategy import IndexingStrategy
from .sqlite_queries import *

class SQLiteIndexing(IndexingStrategy):
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        try:
            self.cursor.execute(CREATE_TABLE)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_image_path(self, path):
        try:
            self.cursor.execute(INSERT_IMAGE_PATH, (path,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding image path: {e}")

    def get_detected_objects(self, path):
        try:
            self.cursor.execute(SELECT_DETECTED_OBJECTS, (path,))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except sqlite3.Error as e:
            print(f"Error getting detected objects: {e}")
            return None

    def get_images_with_all_objects(self, objects):
        try:
            query = SELECT_IMAGES_ALL_OBJECTS.format(' AND '.join(['detected_objects LIKE ?'] * len(objects)))
            self.cursor.execute(query, ['%{}%'.format(obj) for obj in objects])
            results = self.cursor.fetchall()
            return [result[0] for result in results]
        except sqlite3.Error as e:
            print(f"Error getting images with all objects: {e}")
            return []

    def get_images_with_any_objects(self, objects):
        try:
            query = SELECT_IMAGES_ANY_OBJECTS.format(' OR '.join(['detected_objects LIKE ?'] * len(objects)))
            self.cursor.execute(query, ['%{}%'.format(obj) for obj in objects])
            results = self.cursor.fetchall()
            return [result[0] for result in results]
        except sqlite3.Error as e:
            print(f"Error getting images with any objects: {e}")
            return []
