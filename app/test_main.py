from app.main import get_human_age


def test_main_get_0_human_age_for_0_animal_age():
    cat_to_human_age, dog_to_human_age = get_human_age(0, 0)
    assert cat_to_human_age == dog_to_human_age == 0


def test_main_get_0_human_age_for_less_than_15_animal_age():
    cat_to_human_age, dog_to_human_age = get_human_age(14, 14)
    assert cat_to_human_age == dog_to_human_age == 0


def test_main_get_1_human_age_for_less_than_24_animal_age():
    cat_to_human_age, dog_to_human_age = get_human_age(23, 23)
    assert cat_to_human_age == dog_to_human_age == 1


def test_main_get_2_human_age_for_less_than_28_animal_age():
    cat_to_human_age, dog_to_human_age = get_human_age(27, 27)
    assert cat_to_human_age == dog_to_human_age == 2


def test_main_get_3_human_age_for_28_cat_age_and_2_human_age_for_28_dog_age():
    cat_to_human_age, dog_to_human_age = get_human_age(28, 28)
    assert cat_to_human_age == 3 and dog_to_human_age == 2
