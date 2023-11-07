import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.managers.image_search.image_search_manager import ImageSearchManager

import pytest

def test_image_search_manager():
    pass
