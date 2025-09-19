import pytest
from app.main import get_human_age


def test_get_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]

def test_get_human_age_before_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]

def test_get_human_age_exact_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]

def test_get_human_age_next_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]

def test_get_human_age_cat_and_dog_divergence() -> None:
    assert get_human_age(28, 28) == [3, 2]

def test_get_human_age_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]
