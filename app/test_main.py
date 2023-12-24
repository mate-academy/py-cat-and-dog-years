from app.main import get_human_age


def test_should_return_zeros_when_age_animal_less_than_15():
    list_of_age = get_human_age(0, 0)

    assert list_of_age == [0, 0]


def test_should_return_zeros_when_age_animal_is_14():
    list_of_age = get_human_age(14, 14)

    assert list_of_age == [0, 0]


def test_should_return_one_year_when_age_animal_from_15_to_24():
    list_of_age = get_human_age(15, 15)

    assert list_of_age == [1, 1]


def test_should_return_one_year_when_age_animal_is_23():
    list_of_age = get_human_age(23, 23)

    assert list_of_age == [1, 1]


def test_should_return_two_years_when_age_is_24():
    list_of_age = get_human_age(24, 24)

    assert list_of_age == [2, 2]


def test_should_return_two_years_when_age_of_animals_is_28_and_29():
    list_of_age = get_human_age(28, 29)

    assert list_of_age == [3, 3]


def test_should_return_animals_year_when_animals_are_not_died():
    list_of_age = get_human_age(100, 100)

    assert list_of_age == [21, 17]
