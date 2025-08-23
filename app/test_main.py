import pytest
from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(1, 1) == [15, 15]
    assert get_human_age(2, 2) == [24, 24]
    assert get_human_age(3, 3) == [28, 29]
    assert get_human_age(4, 4) == [32, 34]
    assert get_human_age(5, 5) == [36, 39]
    assert get_human_age(14, 14) == [72, 84]


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 10)
    with pytest.raises(ValueError):
        get_human_age(10, -1)
    with pytest.raises(ValueError):
        get_human_age("15", 10)
    with pytest.raises(ValueError):
        get_human_age(10, "15")
