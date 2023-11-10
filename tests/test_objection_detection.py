import pytest
from src.object_detection import ObjectDetection
from src.object_detection import MobileNetDetector
from src.object_detector import ALL_LABELS
from src.image_access import ImageAccess


@pytest.fixture
def object_detection():
    strategy = MobileNetDetector()
    yield ObjectDetection(strategy)


def test_set_model(object_detection):
    object_detection.set_model(None)
    new_model = object_detection._ObjectDetection__detector_model
    assert new_model is None


def test_add_get_labels(object_detection):
    original_labels = ALL_LABELS.copy()
    labels = ["person"]
    object_detection.add_labels(labels)
    result = object_detection.get_labels()
    assert result[91] == "person"


def test_encode_labels(object_detection):
    label = ["person"]
    result = object_detection.encode_labels(label)
    assert result[0] == True


def test_load_model(object_detection):
    model = object_detection.load_model()
    assert callable(model)


def test_detect_objects(object_detection):
    file_path = "example_images/image4.jpg"
    image_access = ImageAccess(file_path)
    image_data = image_access.read_image()
    result = object_detection.detect_objects(image_data)
    assert "car" in result
