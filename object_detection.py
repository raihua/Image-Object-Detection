class ObjectDetection:
    def __init__(self):
        self.__detector_model = None

    def set_model(self, model):
        self.__detector_model = model

    def add_labels(self, labels):
        return self.__detector_model.add_labels(labels)

    def get_labels(self) -> dict:
        return self.__detector_model.get_labels()

    def encode_labels(self, labels) -> list:
        return self.__detector_model.encode_labels(labels)

    def load_model(self):
        return self.__detector_model.load_model()

    def detect_objects(self, image) -> set:
        return self.__detector_model.detect_objects(image)

    detector_model = property(set_model)
