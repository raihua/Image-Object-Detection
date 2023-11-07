import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.engines.object_detection.mobile_net_detector import MobileNetDetector

import pytest

def test_detector_instantiable():
    assert MobileNetDetector()
