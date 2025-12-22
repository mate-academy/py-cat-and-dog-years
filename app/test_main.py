from app.main import get_human_age


def test_should_return_0_when_age_lower_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_when_age_upper_15_and_lower_24() -> None:
    assert get_human_age(15, 23) == [1, 1]


def test_should_return_2years_for_both() -> None:
    assert get_human_age(24, 27) == [2, 2]


def test_should_return_dogs_3rd_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_dogs_correct_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
