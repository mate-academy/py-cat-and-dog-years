from app.main import get_human_age


def test_cat_age_up_to_first_15_years():
    for cat_age in range(15):
        assert get_human_age(cat_age, 0) == [0, 0]


def test_dog_age_up_to_first_15_years():
    for dog_age in range(15):
        assert get_human_age(0, dog_age) == [0, 0]


def test_cat_age_next_9_years():
    for cat_age in range(15, 24):
        assert get_human_age(cat_age, 0) == [1, 0]


def test_dog_age_next_9_years():
    for dog_age in range(15, 24):
        assert get_human_age(0, dog_age) == [0, 1]


def test_cat_age_every_4_years_first_time():
    for cat_age in range(24, 28):
        assert get_human_age(cat_age, 0) == [2, 0]


def test_dog_age_every_5_years_first_time():
    for dog_age in range(24, 29):
        assert get_human_age(0, dog_age) == [0, 2]


def test_dog_cat_age_28_29_years():
    assert get_human_age(28, 29) == [3, 3]


def test_dog_cat_age_100_100_years():
    assert get_human_age(100, 100) == [21, 17]
