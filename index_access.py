class IndexAccess:
    def __init__(self):
        self.__strategy = None

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def add_image_path(self, path):
        self.__strategy.add_image_path(path)

    def add_detected_objects(self, image_path, objects):
        self.__strategy.add_detected_objects(image_path, objects)

    def get_images_with_all_objects(self, objects) -> dict:
        return self.__strategy.get_images_with_all_objects(objects)

    def get_images_with_some_objects(self, objects) -> dict:
        return self.__strategy.get_images_with_some_objects(objects)

    def get_all_images_and_objects(self) -> dict:
        return self.__strategy.get_all_images_and_objects()

    strategy = property(set_strategy)
