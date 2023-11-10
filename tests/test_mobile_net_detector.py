import pytest
from src.mobile_net_detector import MobileNetDetector
from src.object_detector import ALL_LABELS
from src.image_access import ImageAccess


@pytest.fixture
def mobile_net_detector():
    yield MobileNetDetector()


def test_get_labels(mobile_net_detector):
    result = mobile_net_detector.get_labels()
    expected_result = ALL_LABELS
    assert result == expected_result


def test_add_labels(mobile_net_detector):
    labels = ["person"]
    mobile_net_detector.add_labels(labels)
    result = mobile_net_detector.get_labels()
    assert result[91] == "person"


def test_encode_labels(mobile_net_detector):
    label = ["person"]
    result = mobile_net_detector.encode_labels(label)
    assert result[0] == True


def test_load_model(mobile_net_detector):
    model = mobile_net_detector.load_model()
    assert callable(model)


def test_detect_objects(mobile_net_detector):
    file_path = "example_images/image4.jpg"
    image_access = ImageAccess(file_path)
    image_data = image_access.read_image()
    result = mobile_net_detector.detect_objects(image_data)
    assert "car" in result
