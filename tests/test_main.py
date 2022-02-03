from app.main import get_human_age


def test_first_fifteen_years_for_cat():
    actual = get_human_age(15, 14)
    assert actual == [1, 0]


def test_first_fifteen_years_for_dog():
    actual = get_human_age(14, 15)
    assert actual == [0, 1]


def test_next_nine_years_for_pets():
    actual = get_human_age(24, 24)
    assert actual == [2, 2]


def test_every_four_next_years_for_cat():
    actual = get_human_age(28, 28)
    assert actual == [3, 2]


def test_every_five_next_years_for_dog():
    actual = get_human_age(29, 29)
    assert actual == [3, 3]
