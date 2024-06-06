import pytest
from app.main import get_human_age


def test_get_human_age_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0], "Both cat and dog ages are zero"


def test_get_human_age_just_below_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0], (
        "Both cat and dog ages are just below first human year"
    )


def test_get_human_age_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1], (
        "Both cat and dog ages are at first human year"
    )


def test_get_human_age_just_below_second_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1], (
        "Both cat and dog ages are just below second human year"
    )


def test_get_human_age_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2], (
        "Both cat and dog ages are at second human year"
    )


def test_get_human_age_just_below_third_human_year() -> None:
    assert get_human_age(27, 27) == [2, 2], (
        "Both cat and dog ages are just below third human year"
    )


def test_get_human_age_third_human_year() -> None:
    assert get_human_age(28, 28) == [3, 2], (
        "Cat age is at third human year and dog age is just below third "
    )


def test_get_human_age_large_years() -> None:
    assert get_human_age(100, 100) == [21, 17], (
        "Both cat and dog ages are large"
    )


if __name__ == "__main__":
    pytest.main()
