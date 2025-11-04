from app.main import get_human_age

def test_should_return_zero_if_animal_age_lower_than_zero():
    cat_age, dog_age = -1, -2
    result = get_human_age(cat_age, dog_age)
    assert result == [0, 0]

def test_should_return_one_year_if_age_equal_first_year():
    cat_age, dog_age = 15, 15
    result = get_human_age(cat_age, dog_age)
    assert result == [1, 1]

def test_24_catdog_years_should_convert_into_2_human_age():
    cat_age, dog_age = 24, 24
    result = get_human_age(cat_age, dog_age)
    assert result == [2, 2]

def test_14_catdog_years_should_convert_into_0_human_age():
    cat_age, dog_age = 14, 14
    result = get_human_age(cat_age, dog_age)
    assert result == [0, 0]

def test_23_catdog_years_should_convert_into_1_human_age():
    cat_age, dog_age = 23, 23
    result = get_human_age(cat_age, dog_age)
    assert result == [1, 1]

def test_27_28_catdog_years_should_convert_into_2_human_age():
    cat_age, dog_age = 27, 28
    result = get_human_age(cat_age, dog_age)
    assert result == [2, 2]

def test_28_29_catdog_years_should_convert_into_3_human_age():
    cat_age, dog_age = 28, 29
    result = get_human_age(cat_age, dog_age)
    assert result == [3, 3]