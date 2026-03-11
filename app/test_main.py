from app.main import get_human_age


def test_zero_ages():
    assert get_human_age(0, 0) == [0, 0]


def test_fourteen_years_are_still_zero():
    assert get_human_age(14, 14) == [0, 0]


def test_fifteen_years_convert_to_one():
    assert get_human_age(15, 15) == [1, 1]


def test_twenty_three_years_are_still_one():
    assert get_human_age(23, 23) == [1, 1]


def test_twenty_four_years_convert_to_two():
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_have_different_step_sizes_after_twenty_four():
    assert get_human_age(27, 28) == [2, 2]


def test_next_full_step_after_twenty_four():
    assert get_human_age(28, 29) == [3, 3]


def test_large_ages():
    assert get_human_age(100, 100) == [21, 17]
