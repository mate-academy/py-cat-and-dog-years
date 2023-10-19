from app.main import get_human_age


def test_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_then_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_one_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_a_few_year() -> None:
    assert get_human_age(28, 28) == [3, 2]
