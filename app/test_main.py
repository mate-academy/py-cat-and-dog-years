from app.main import get_human_age


def test_should_return_zero_for_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_under_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_human_year_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_second_threshold_before_increment() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_second_human_year_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_before_next_increment() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_next_increment_cat_faster_than_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_cat_extra_years_every_4() -> None:
    assert get_human_age(32, 0)[0] == 4


def test_cat_extra_years_every_5() -> None:
    assert get_human_age(0, 34)[1] == 4
