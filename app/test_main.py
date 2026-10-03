from app.main import get_human_age


def test_should_return_zero_for_ages_less_than_15() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_for_ages_from_15_to_23() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_at_age_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_handle_cat_and_dog_boundaries_differently() -> None:
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(29, 29) == [3, 3]


def test_should_discard_remainder() -> None:
    assert get_human_age(31, 33) == [3, 3]
    assert get_human_age(32, 34) == [4, 4]


def test_should_convert_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_should_calculate_cat_and_dog_ages_independently() -> None:
    assert get_human_age(28, 24) == [3, 2]
    assert get_human_age(24, 29) == [2, 3]
