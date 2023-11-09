from sqlite_indexing import SQLiteIndexing


class IndexAccess:
    def __init__(self, strategy=SQLiteIndexing()):
        self.__strategy = strategy

    def get_strategy(self):
        return self.__strategy

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def add_image_path(self, path):
        self.__strategy.add_image_path(path)

    def add_detected_objects(self, image_path, objects):
        self.__strategy.add_detected_objects(image_path, objects)

    def get_images_with_all_objects(self, objects):
        return self.__strategy.get_images_with_all_objects(objects)

    def get_images_with_some_objects(self, objects):
        return self.__strategy.get_images_with_some_objects(objects)

    strategy = property(get_strategy, set_strategy)
