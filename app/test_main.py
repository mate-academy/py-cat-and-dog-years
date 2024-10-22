from app.main import get_human_age

def test_should_return_zero_if_cat_and_dog_age_equal_14():
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_extra_human_year_after_24_animal_years():
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_5_human_years_if_cat_years_equals_36():
    assert get_human_age(36, 28) == [5, 2]


def test_should_return_6_human_years_if_dog_years_equals_44():
    assert get_human_age(36, 44) == [5, 6]
