from app.main import get_human_age


def test_age_under_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_in_the_first_range_1() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_in_the_first_range_2() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_in_the_second_range_1() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_age_in_the_second_range_2() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_age_in_the_third_range_1() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_age_in_the_third_range_2() -> None:
    assert get_human_age(31, 33) == [3, 3]


def test_age_in_the_fourth_range() -> None:
    assert get_human_age(32, 34) == [4, 4]
