import pytest
from app.main import get_human_age


def test_incorrect_year_format() -> None:
    with pytest.raises(ValueError):
        get_human_age(-12, 43.1)


def test_with_zero_expected():
    assert get_human_age(12, 14) == [0, 0]


def test_with_extra_years():
    assert get_human_age(28, 27) == [3, 2]


def test_with_more_than_100_years():
    assert get_human_age(100, 100) == [21, 17]
