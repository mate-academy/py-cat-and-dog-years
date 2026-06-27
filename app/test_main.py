from app.main import get_human_age


def test_zero_equals_zero() -> None:
    assert get_human_age(cat_age=0, dog_age=0) == [0, 0]


def test_fourteen_equal_fourteen() -> None:
    assert get_human_age(cat_age=14, dog_age=14) == [0, 0]


def test_fifteen_equal_one_one() -> None:
    assert get_human_age(cat_age=15, dog_age=15) == [1, 1]


def test_twenty_four_equal_two_two() -> None:
    assert get_human_age(cat_age=24, dog_age=24) == [2, 2]


def test_twenty_eight_equal_three_two() -> None:
    assert get_human_age(cat_age=28, dog_age=28) == [3, 2]


def test_one_hundred_equal_twenty_one_and_seventeen() -> None:
    assert get_human_age(cat_age=100, dog_age=100) == [21, 17]
