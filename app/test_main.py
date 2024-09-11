from app.main import get_human_age

def test_should_return_0_human_years_for_14_cat_dog_years():
    assert get_human_age(14, 14) == [0, 0]


