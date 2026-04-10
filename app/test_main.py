from app.main import get_human_age


def test_cat_age_and_dog_age_are_both_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_cat_age_and_dog_age_equal_one_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_cat_age_and_dog_age_equal_two_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_value_slightly_less_the_first_limit() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_between_first_and_second_limit() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_on_the_border_of_the_next_block_without_cat() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_on_the_verge_of_transition_to_next_block_cat_gets_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_number_for_checking_multiple_block_repetitions() -> None:
    assert get_human_age(100, 100) == [21, 17]
