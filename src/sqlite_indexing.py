from src.index_strategy import IndexStrategy
import sqlite3

class SQLiteIndexing(IndexStrategy):
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(self.db)

    def add_image_path(self, path):
        pass

    def get_detected_objects(self, path):
        pass

    def get_images_with_all_objects(self, objects):
        pass

    def get_images_with_some_objects(self, objects):
        pass
