from app.main import get_human_age


def test_get_human_age_where_age_is_a_whole_number():
    assert isinstance(get_human_age(100, 100)[0], int)
    assert isinstance(get_human_age(100, 100)[1], int)


def test_get_human_age_check_cat_years_are_converted_correctly():
    assert get_human_age(14, 14)[0] == 0
    assert get_human_age(15, 15)[0] == 1
    assert get_human_age(24, 24)[0] == 2
    assert get_human_age(28, 28)[0] == 3
    assert get_human_age(100, 100)[0] == 21


def test_get_human_age_check_dog_years_are_converted_correctly():
    assert get_human_age(14, 14)[1] == 0
    assert get_human_age(15, 15)[1] == 1
    assert get_human_age(24, 24)[1] == 2
    assert get_human_age(28, 28)[1] == 2
    assert get_human_age(100, 100)[1] == 17

