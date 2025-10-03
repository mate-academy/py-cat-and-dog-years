from app.main import get_human_age


def test_zero_ages_should_return_zero_human_years():
    assert get_human_age(0, 0) == [0, 0]


def test_just_below_first_threshold_should_return_zero():
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_first_threshold_should_return_one():
    assert get_human_age(15, 15) == [1, 1]


def test_just_below_second_threshold_should_still_return_one():
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_second_threshold_should_return_two():
    assert get_human_age(24, 24) == [2, 2]


def test_just_below_third_threshold_should_still_return_two():
    assert get_human_age(27, 27) == [2, 2]


def test_cat_crosses_third_threshold_but_dog_does_not():
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages_should_return_expected_human_years():
    assert get_human_age(100, 100) == [21, 17]
