from app.main import get_human_age


def test_should_return_list_with_two_elements() -> None:
    assert len(get_human_age(14, 18)) == 2


def test_result_in_list_is_integer() -> None:
    result = get_human_age(17, 17)
    assert isinstance(result[0], int) and isinstance(result[1], int) is True


def test_should_return_list_with_two_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_list_with_two_ones_when_age_between_15_and_24() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_list_with_two_twos() -> None:
    assert get_human_age(26, 28) == [2, 2]


def test_should_return_list_with_two_threes() -> None:
    assert get_human_age(28, 29) == [3, 3]
