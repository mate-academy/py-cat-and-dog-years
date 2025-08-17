from app.main import get_human_age


def test_should_return_zeros_if_value_is_0() -> None:
    result = get_human_age(0, 0)
    assert result == [0, 0]


def test_should_return_zeros_if_value_is_less_than_15() -> None:
    result = get_human_age(14, 14)
    assert result == [0, 0]


def test_should_correctly_konvert_different_ages() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]


def test_age_should_be_a_whole_number_of_years() -> None:
    result = get_human_age(100, 100)
    assert result == [21, 17]
