import pytest
from image_search_manager import ImageSearchManager
from unittest.mock import Mock


@pytest.fixture
def output_formatter():
    return Mock()


@pytest.fixture
def object_detection():
    return Mock()


@pytest.fixture
def index_access():
    return Mock()


@pytest.fixture
def image_access():
    return Mock()


@pytest.fixture
def matching_engine():
    return Mock()


@pytest.fixture
def image_search_manager(
        output_formatter,
        object_detection,
        index_access,
        image_access,
        matching_engine):
    return ImageSearchManager(output_formatter, object_detection, index_access, image_access, matching_engine)

