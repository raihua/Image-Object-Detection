import pytest
from src.object_detection import ObjectDetection


@pytest.fixture
def object_detection():
    yield ObjectDetection()

def test_set_model(object_detection):
    object_detection.set_model(None)
    new_model = object_detection.detector_model
    assert new_model is None

