from app.main import get_human_age


def test_check_if_animal_age_is_zero():
    goal = get_human_age(14, 14)
    assert goal == [0, 0]


def test_check_if_animal_age_is_one():
    goal = get_human_age(15, 15)
    assert goal == [1, 1]


def test_check_if_animal_age_is_two():
    goal = get_human_age(27, 27)
    assert goal == [2, 2]


def test_check_when_dog_and_cat_have_different_age():
    goal = get_human_age(28, 28)
    assert goal == [3, 2]
