from app.main import get_human_age


def test_get_human_age_years_should_convert_into_1():
    assert get_human_age(15, 15) == [1, 1]

def test_get_human_age_years_should_convert_into_2():
    assert get_human_age(24, 24) == [2, 2]

def test_get_human_age_years_should_convert_into_3():
    assert get_human_age(28, 29) == [3, 3]