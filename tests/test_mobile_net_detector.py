import pytest
from src.mobile_net_detector import MobileNetDetector

@pytest.fixture
def mobile_net_detector():
    return MobileNetDetector()


def test_add_labels():
    labels = ["person"]

    