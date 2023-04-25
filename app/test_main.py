from app.main import get_human_age


def test_one_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_two_human_years() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_three_human_years() -> None:
    assert get_human_age(29, 29) == [3, 3]


def test_extra_human_years() -> None:
    assert get_human_age(50, 50) == [8, 7]
