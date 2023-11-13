import pytest
from unittest.mock import Mock, create_autospec
from output_formatter import OutputFormatter
from object_detection import ObjectDetection
from index_access import IndexAccess
from image_access import ImageAccess
from matching_engine import MatchingEngine
from image_search_manager import ImageSearchManager
from image_search_manager_builder import ImageSearchManagerBuilder

@pytest.fixture
def output_formatter():
    return create_autospec(OutputFormatter)

@pytest.fixture
def object_detection():
    return create_autospec(ObjectDetection)

@pytest.fixture
def index_access():
    return create_autospec(IndexAccess)

@pytest.fixture
def image_access():
    return create_autospec(ImageAccess)

@pytest.fixture
def matching_engine():
    return create_autospec(MatchingEngine)

def test_image_search_manager_builder(
        output_formatter, object_detection, index_access, image_access, matching_engine):
    # Mock strategies
    index_strategy = Mock()
    object_detection_model = Mock()
    matching_strategy = Mock()

    builder = ImageSearchManagerBuilder()
    builder.output_formatter = output_formatter
    builder.object_detection = object_detection
    builder.index_access = index_access
    builder.image_access = image_access
    builder.matching_engine = matching_engine

    builder.set_index_strategy(index_strategy)
    builder.set_object_detection_model(object_detection_model)
    builder.set_matching_strategy(matching_strategy)

    # Build ImageSearchManager
    image_search_manager = builder.build()

    assert isinstance(image_search_manager, ImageSearchManager)
    index_access.set_strategy.assert_called_with(index_strategy)
    object_detection.set_model.assert_called_with(object_detection_model)
    matching_engine.set_strategy.assert_called_with(matching_strategy)
