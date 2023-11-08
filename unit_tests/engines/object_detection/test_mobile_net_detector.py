import pytest
from ... import project_root
from src.engines.object_detection.mobile_net_detector import MobileNetDetector

def test_detector_instantiable():
    assert MobileNetDetector()
