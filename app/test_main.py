from app.main import get_human_age


def test_should_return_list():
    years = get_human_age(10, 8)
    assert isinstance(years, list)


def test_two_pats_of_list_should_be_integer():
    years = get_human_age(10, 8)
    cat_years = years[0]
    dog_years = years[1]
    assert isinstance(cat_years, int) and isinstance(dog_years, int)


def test_length_of_the_list_must_be_equal_to_two():
    years = get_human_age(10, 8)
    assert len(years) == 2


def test_should_return_zero_when_cat_and_dog_years_less_than_15():
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_human_year_when_cat_and_dog_years_are_equal_to_15():
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_1_human_year_when_cat_and_dog_years_less_than_24():
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_human_years_when_cat_and_dog_years_are_equal_to_24():
    assert get_human_age(24, 24) == [2, 2]


def test_27_cat_and_28_dog_years_should_return_2_human_years():
    assert get_human_age(24, 24) == [2, 2]


def test_28_cat_and_29_dog_years_should_return_3_human_years():
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_expected_years():
    assert get_human_age(100, 100) == [21, 17]
