from abc import ABC, abstractmethod


class IndexStrategy(ABC):
    @abstractmethod
    def add_image_path(self, path):
        pass

    @abstractmethod
    def get_images_with_all_objects(self, objects):
        pass

    @abstractmethod
    def get_images_with_some_objects(self, objects):
        pass