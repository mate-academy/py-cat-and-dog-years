from app import main


def test_should_return_two_elements():
    result = main.get_human_age(10, 10)
    assert len(result) == 2


def test_should_return_zero_when_both_arg_are_zero() -> None:
    result = main.get_human_age(0, 0)
    assert result == [0, 0]


def test_should_return_zero_when_age_less_fifteen() -> None:
    assert main.get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_age_fifteen() -> None:
    assert main.get_human_age(15, 15) == [1, 1]


def test_should_return_one_when_age_is_twenty_three() -> None:
    assert main.get_human_age(23, 23) == [1, 1]


def test_should_return_two_year_when_age_twentyfour() -> None:
    assert main.get_human_age(24, 24) == [2, 2]


def test_should_return_two_when_age_twentyseven() -> None:
    assert main.get_human_age(27, 27) == [2, 2]


def test_should_return_two_cats_and_two_dogs() -> None:
    assert main.get_human_age(27, 28) == [2, 2]


def test_should_return_three_cats_and_two_dogs() -> None:
    assert main.get_human_age(28, 28) == [3, 2]


def test_should_return_three_for_cat_28_and_dog_29() -> None:
    assert main.get_human_age(28, 29) == [3, 3]


def test_should_return_correct_human_age_for_large_numbers() -> None:
    assert main.get_human_age(100, 100) == [21, 17]


def test_should_return_three_cats_and_two_dogs_when_cat_boundary() -> None:
    assert main.get_human_age(28, 24) == [3, 2]


def test_should_return_two_cats_and_three_dogs_when_dog_boundary() -> None:
    assert main.get_human_age(24, 29) == [2, 3]
