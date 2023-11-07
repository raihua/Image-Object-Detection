import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.managers.image_search.image_search_manager import ImageSearchManager

import pytest

@pytest.fixture
def manager():
    return ImageSearchManager()

def test_manager_add(manager):
    manager.add("example_images/image4.jpg")

def test_manager_add_boundary(manager):
    with pytest.raises(TypeError):
        manager.add(5)
        manager.add(5.0)
        manager.add()