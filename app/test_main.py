from app.main import get_human_age


def test_should_return_zeros_when_age_is_0():
    list_of_age = get_human_age(0, 0)

    assert list_of_age == [0, 0]


def test_should_return_one_year_when_age_is_15():
    list_of_age = get_human_age(15, 15)

    assert list_of_age == [1, 1]


def test_should_return_two_years_when_age_is_24():
    list_of_age = get_human_age(24, 24)

    assert list_of_age == [2, 2]


def test_should_return_cat_years_when_age_is_28():
    list_of_age = get_human_age(28, 0)

    assert list_of_age == [3, 0]


def test_should_return_dog_years_when_age_is_28():
    list_of_age = get_human_age(0, 29)

    assert list_of_age == [0, 3]
