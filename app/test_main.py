from app.main import get_human_age


def test_should_equal_to_zero() -> None:
    cat_to_human = 0
    dog_to_human = 0
    assert get_human_age(cat_to_human, dog_to_human) == [0, 0]


def test_one_human_year_should_equal_below_15_year_of_both() -> None:
    cat_to_human = 14
    dog_to_human = 14
    assert get_human_age(cat_to_human, dog_to_human) == [0, 0]


def test_one_human_year_should_equal_15_year_of_both() -> None:
    cat_to_human = 15
    dog_to_human = 15
    assert get_human_age(cat_to_human, dog_to_human) == [1, 1]


def test_one_human_year_should_equal_below_24_year_of_both() -> None:
    cat_to_human = 23
    dog_to_human = 23
    assert get_human_age(cat_to_human, dog_to_human) == [1, 1]


def test_second_human_year_should_add_9_years_of_both() -> None:
    cat_to_human = 24
    dog_to_human = 24
    assert get_human_age(cat_to_human, dog_to_human) == [2, 2]


def test_next_human_years_should_add_4_cat_years_and_5_dog_years() -> None:
    cat_to_human = 28
    dog_to_human = 29
    assert get_human_age(cat_to_human, dog_to_human) == [3, 3]
