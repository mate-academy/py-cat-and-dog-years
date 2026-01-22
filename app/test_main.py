from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_just_before_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_first_and_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_between_second_and_third_threshold() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_exactly_third_threshold() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_big_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_returns_list_of_two_ints() -> None:
    result = get_human_age(50, 50)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
