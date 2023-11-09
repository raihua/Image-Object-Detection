import pytest
from src.object_detection import ObjectDetection
from src.object_detection import MobileNetDetector
from src.object_detector import ALL_LABELS
from src.image_access import ImageAccess

all_labels_original = ALL_LABELS

@pytest.fixture
def object_detection():
    yield ObjectDetection(MobileNetDetector())

def test_set_model(object_detection):
    object_detection.set_model(None)
    new_model = object_detection.detector_model
    assert new_model is None

def test_get_model(object_detection):
    model = object_detection.get_model()
    assert isinstance(model, MobileNetDetector)

def test_get_labels(object_detection):
    labels = object_detection.get_labels()
    expected_labels = all_labels_original
    assert labels == expected_labels

def test_add_labels(object_detection):
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