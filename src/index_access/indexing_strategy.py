from abc import ABC, abstractmethod

class IndexingStrategy(ABC):
    @abstractmethod
    def add_image_path(self, path):
        pass

    @abstractmethod
    def get_detected_objects(self, path):
        pass

    @abstractmethod
    def get_images_with_all_objects(self, objects):
        pass

    @abstractmethod
    def get_images_with_any_objects(self, objects):
        pass

