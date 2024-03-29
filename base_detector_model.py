from abc import ABC, abstractmethod


class BaseDetectorModel(ABC):
    @abstractmethod
    def encode_labels(self, labels) -> list:
        pass

    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def detect_objects(self, image) -> set:
        pass

    @abstractmethod
    def add_labels(self, labels):
        pass

    @abstractmethod
    def get_labels(self) -> dict:
        pass
