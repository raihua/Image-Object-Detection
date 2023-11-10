import pytest
import numpy as np
from src.matching_engine import MatchingEngine
from src.cosine_similarity import CosineSimilarity


@pytest.fixture
def matching_engine():
    strategy = CosineSimilarity()
    yield MatchingEngine(strategy)


def test_set_strategy(matching_engine):
    matching_engine.set_strategy(None)
    strategy = matching_engine._MatchingEngine__strategy
    assert strategy is None


def test_calculate_similarity(matching_engine):
    original_array = np.array([[1, 2], [3, 4]])
    flattened_array = original_array.flatten().reshape(1, -1)
    result = matching_engine._MatchingEngine__calculate_similarity(flattened_array, flattened_array)
    assert result == pytest.approx(1)


def test_execute_matching(matching_engine):
    image = np.array([1, 2, 3]).flatten().reshape(1, -1)
    image_dict = (
        ("example.jpg", [1, 2, 3]),
    )
    results = matching_engine.execute_matching(image, image_dict)
    expected_result = (("example.jpg", 1)),
    assert results == expected_result
