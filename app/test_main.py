from app.main import get_human_age


def test_human_age_is_int():
    age = get_human_age(1, 150)
    assert isinstance(age[0], int) is True \
           and isinstance(age[1], int) is True


def test_should_return_0_if_animal_age_is_0():
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_0_if_animal_age_is_under_15():
    assert get_human_age(8, 12) == [0, 0]


def test_should_return_1_if_animal_age_is_between_15_and_23():
    assert get_human_age(23, 15) == [1, 1]


def test_if_cat_older_than_23_add_1_every_4_years():
    assert get_human_age(28, 0) == [3, 0]
    assert get_human_age(36, 28) == [5, 2]


def test_if_dog_older_than_23_add_1_every_5_years():
    assert get_human_age(0, 29) == [0, 3]
    assert get_human_age(24, 39) == [2, 5]


def test_should_work_correct_with_big_numbers():
    assert get_human_age(100, 100) == [21, 17]
