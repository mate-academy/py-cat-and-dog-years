from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_first_year_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_second_year_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_third_year_increment() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]


def test_all_elements_are_integers() -> None:
    assert all(isinstance(x, int) for x in get_human_age(0, 0))
    assert all(isinstance(x, int) for x in get_human_age(15, 15))
    assert all(isinstance(x, int) for x in get_human_age(100, 100))
