from app.main import get_human_age


def test_check_if_return_list():
    age = get_human_age(0, 0)

    assert isinstance(age, list)


def test_check_year_equil_null():
    age = get_human_age(0, 0)

    assert age == [0, 0]


def test_check_year_less_than_15():
    age = get_human_age(14, 14)

    assert age == [0, 0]


def test_check_year_equil_15():
    age = get_human_age(15, 15)

    assert age == [1, 1]


def test_check_year_after_9_years_more():
    age = get_human_age(24, 24)

    assert age == [2, 2]


def test_check_year_after_4_years_more():
    age = get_human_age(28, 28)

    assert age == [3, 2]
