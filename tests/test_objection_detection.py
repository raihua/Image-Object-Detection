import pytest
from src.object_detection import ObjectDetection
from src.mobile_net_detector import MobileNetDetector
from src.object_detector import ALL_LABELS


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

# def test_get_labels(object_detection):
#     labels = object_detection.get_labels()
#     expected_labels = ALL_LABELS
#     assert labels == expected_labels


