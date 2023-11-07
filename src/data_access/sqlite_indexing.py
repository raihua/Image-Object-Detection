from indexing_strategy import IndexingStrategy

class SQLiteIndexing(IndexingStrategy):
    def __init__(self, conn):
        self.conn = conn

    def add_image_path(self, path):
        pass

    def get_detected_objects(self, path):
        pass

    def get_images_with_all_objects(self, objects):
        pass

    def get_images_with_any_objects(self, objects):
        pass
