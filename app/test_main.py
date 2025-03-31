from app.main import get_human_age
import pytest


def test_get_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0], \
        "Expected [0, 0] for 0 cat and 0 dog age"


def test_get_human_age_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0], \
        "Expected [0, 0] for 14 cat and 14 dog age"


def test_get_human_age_second_year() -> None:
    assert get_human_age(23, 23) == [1, 1], \
        "Expected [1, 1] for 23 cat and 23 dog age"


def test_get_human_age_third_year_cat() -> None:
    assert get_human_age(28, 0) == [3, 0], \
        "Expected [3, 0] for 28 cat age and 0 dog age"


def test_get_human_age_third_year_dog() -> None:
    assert get_human_age(0, 29) == [0, 3], \
        "Expected [0, 3] for 0 cat age and 29 dog age"


def test_get_human_age_mixed_values() -> None:
    assert get_human_age(44, 49) == [7, 7], \
        "Expected [7, 7] for 44 cat age and 49 dog age"


def test_get_human_age_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17], \
        "Expected [21, 17] for 100 cat and 100 dog age"


def test_get_human_age_negative_ages() -> None:
    assert get_human_age(-1, -5) == [0, 0], "Negative ages should return 0"


def test_get_human_age_invalid_cat_age_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("ten", 20)
    assert True, "TypeError when age is str"


def test_get_human_age_none_ages() -> None:
    with pytest.raises(TypeError):
        get_human_age(None, 10.2)
    assert True, "TypeError when age is None"
