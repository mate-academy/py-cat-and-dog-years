import pytest

from app.main import get_human_age


def test_get_human_age_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_1() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_2() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_3_and_2() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_large_value() -> None:
    assert get_human_age(1000, 1000) == [246, 197]


def test_get_human_age_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")

    with pytest.raises(TypeError):
        get_human_age(None, 10)


def test_get_human_age_value_error() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, -1)
