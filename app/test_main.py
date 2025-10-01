from app.main import get_human_age


def test_when_age_lower_than_first_year() -> None:
    assert get_human_age(0, 14) == [0, 0]


def test_different_each_year() -> None:
    assert get_human_age(100, 1000) == get_human_age(21, 17)


def check_integer() -> None:
    assert all(isinstance(x, int) for x in get_human_age(28, 28))