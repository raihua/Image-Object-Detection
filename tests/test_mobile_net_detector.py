import pytest
from src.mobile_net_detector import MobileNetDetector
from src.object_detector import ALL_LABELS

@pytest.fixture
def mobile_net_detector():
    return MobileNetDetector()


def test_add_labels(mobile_net_detector):
    labels = ["person"]
    mobile_net_detector.add_labels(labels)
    result = mobile_net_detector.get_labels()
    assert result[91] == "person"

def test_get_labels(mobile_net_detector):
    result = mobile_net_detector.get_labels()
    expected_result = ALL_LABELS
    assert result == expected_result

def test_encode_labels(mobile_net_detector):
    label = ["person"]
    result = mobile_net_detector.encode_labels(label)
    assert result[0] == True

