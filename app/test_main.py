from app.main import get_human_age


def test_cat_and_god_years_convert():
    assert get_human_age(100, 100) == [21, 17]
