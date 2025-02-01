from app.main import get_human_age

# write your code here
def test_should_convert_first_15_years_animals_to_1_human() -> None:
    cat_age = 15
    dog_age = 15
    res = get_human_age(cat_age, dog_age)
    assert (res == [1, 1])

def test_should_convert_second_9_years_animals_to_1_human() -> None:
    cat_age = 24
    dog_age = 24
    res = get_human_age(cat_age, dog_age)
    assert (res == [2, 2])

def test_should_convert_every_next_5_years_for_cat_and_4_years_for_dog_to_1_human() -> None:
    cat_age = 100
    dog_age = 100
    res = get_human_age(cat_age, dog_age)
    assert (res == [21, 17])

def test_should_convert_discard_the_remainder() -> None:
    cat_age = 14
    dog_age = 14
    res = get_human_age(cat_age, dog_age)
    assert (res == [0, 0])

def test_23_cat_and_dog_years_should_convert_into_1_human_age() -> None:
    cat_age = 23
    dog_age = 23
    res = get_human_age(cat_age, dog_age)
    assert (res == [1, 1])

