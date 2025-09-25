import pytest
from app.main import get_human_age


# ✅ Casos básicos
def test_get_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_fourteen() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_exact_threshold() -> None:
    assert get_human_age(24, 24) == [1, 1]


def test_get_human_age_next_threshold() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_28() -> None:
    assert get_human_age(28, 28) == [2, 2]


def test_get_human_age_cat_and_dog_divergence() -> None:
    assert get_human_age(35, 30) == [3, 2]


def test_get_human_age_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]


# ❌ Casos inválidos (sem parametrize)
def test_invalid_negative_cat() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 5)


def test_invalid_negative_dog() -> None:
    with pytest.raises(ValueError):
        get_human_age(5, -1)


def test_invalid_both_negative() -> None:
    with pytest.raises(ValueError):
        get_human_age(-3, -3)


def test_invalid_float_input() -> None:
    with pytest.raises(TypeError):
        get_human_age(3.5, 5)  # type: ignore


def test_invalid_string_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("5", 5)  # type: ignore


def test_invalid_none_input() -> None:
    with pytest.raises(TypeError):
        get_human_age(None, 5)  # type: ignore
