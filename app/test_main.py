from app.main import get_human_age


def test_for_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_for_one_year_age() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_for_two_years_age() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_for_different_age() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_for_more_than_two_years() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_output_is_not_float() -> None:
    for age in get_human_age(15, 87):
        assert isinstance(age, int)
