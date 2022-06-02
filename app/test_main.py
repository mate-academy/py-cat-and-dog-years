from app.main import get_human_age


def test_age_of_animals_with_zeroes():
    assert get_human_age(0, 0) == [0, 0]


def test_age_of_animals_before_15_years():
    assert get_human_age(14, 14) == [0, 0]


def test_age_of_animals_when_age_is_15_years():
    assert get_human_age(15, 15) == [1, 1]


def test_age_of_animals_before_24_years():
    assert get_human_age(23, 23) == [1, 1]


def test_age_of_animals_when_age_is_24_years():
    assert get_human_age(24, 24) == [2, 2]


def test_age_of_animals_before_28_years():
    assert get_human_age(27, 27) == [2, 2]


def test_age_of_animals_when_age_is_28_years():
    assert get_human_age(28, 28) == [3, 2]


def test_age_of_animals_when_age_is_more_than_28():
    assert get_human_age(100, 100) == [21, 17]
