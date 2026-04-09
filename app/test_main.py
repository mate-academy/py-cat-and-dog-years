from app.main import get_human_age


def test_zero_ages():
    assert get_human_age(0, 0) == [0, 0]


def test_first_human_year_boundary():
    assert get_human_age(15, 15) == [1, 1]


def test_second_human_year_boundary():
    assert get_human_age(24, 24) == [2, 2]


def test_remainders_are_discarded():
    assert get_human_age(27, 28) == [2, 2]


def test_cat_and_dog_progress_after_second_boundary():
    assert get_human_age(28, 29) == [3, 3]


def test_large_ages():
    assert get_human_age(100, 100) == [21, 17]
