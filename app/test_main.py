from app.main import get_human_age


def test_should_return_list() -> None:
    years = get_human_age(15, 15)

    assert isinstance(years, list)


def test_should_return_list_of_given_length() -> None:
    years = get_human_age(11, 10)

    assert len(years) == 2


def test_not_positive_human_age() -> None:
    assert get_human_age(-1, -2) == [0, 0]


def test_zero_human_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_one_human_age() -> None:
    assert get_human_age(10, 14) == [0, 0]


def test_one_human_age() -> None:
    assert get_human_age(15, 16) == [1, 1]


def test_two_human_age() -> None:
    assert get_human_age(25, 26) == [2, 2]


def test_different_human_age() -> None:
    assert get_human_age(18, 28) == [1, 2]


def test_should_return_expected_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
