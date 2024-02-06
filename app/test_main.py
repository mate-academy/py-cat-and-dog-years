from app.main import get_human_age


def test_should_return_human_age_less_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_convert_one_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_convert_two_human_age() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_human_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
