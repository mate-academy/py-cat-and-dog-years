from app.main import get_human_age


def test_should_return_list_and_int():
    result = get_human_age(15, 15)
    for year in result:
        assert isinstance(year, (list, int))


def test_28_cat_dog_years_should_convert_to_3_2_human_year():
    assert get_human_age(28, 28) == [3, 2]


def test_24_cat_dog_years_should_convert_into_2_human_ages():
    assert get_human_age(24, 24) == [2, 2]


def test_15_cat_dog_years_should_convert_into_1_human_age():
    assert get_human_age(15, 15) == [1, 1]
