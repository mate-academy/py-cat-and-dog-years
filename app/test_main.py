import pytest

from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]


def test_get_human_age_negative_numbers() -> None:
    assert get_human_age(-5, 10) == [0, 0]
    assert get_human_age(10, -5) == [0, 0]
    assert get_human_age(-5, -5) == [0, 0]


def test_get_human_age_invalid_data_types() -> None:
    # Test when one age is provided as a string
    with pytest.raises(TypeError):
        get_human_age("10", 15)
    with pytest.raises(TypeError):
        get_human_age(10, "15")

    # Test when both ages are provided as strings
    with pytest.raises(TypeError):
        get_human_age("10", "15")

    # Test when one age is None
    with pytest.raises(TypeError):
        get_human_age(None, 15)
    with pytest.raises(TypeError):
        get_human_age(10, None)

    # Test when both ages are None
    with pytest.raises(TypeError):
        get_human_age(None, None)
