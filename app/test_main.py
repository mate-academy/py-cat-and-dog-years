from app.main import get_human_age


def test_should_return_zero_if_age_less_than_first_year() -> None:
    assert get_human_age(13, 13) == [0, 0]


def test_should_return_one_if_age_less_than_first_and_second_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_if_cat_age_more_than_twentyfour_but_less_than_twenty_eight() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_two_if_dog_age_more_than_twentyfour_but_less_than_twenty_nine() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_result_according_to_formulas_for_cat_and_dog() -> None:
    assert get_human_age(100, 100) == [21, 17]