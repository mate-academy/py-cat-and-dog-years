from app.main import get_human_age


def test_animal_age_in_range_0_15():
    assert get_human_age(2, 12) == [0, 0]
    assert get_human_age(10, 0) == [0, 0]


def test_animal_age_in_range_16_23():
    assert get_human_age(16, 22) == [1, 1]
    assert get_human_age(18, 19) == [1, 1]


def test_cat_age_in_range_24_27():
    assert get_human_age(26, 0) == [3, 0]
    assert get_human_age(27, 0) == [3, 0]


def test_dog_age_in_range_24_28():
    assert get_human_age(0, 25) == [0, 3]
    assert get_human_age(0, 26) == [0, 3]


def test_cat_older_then_27_and_dog_older_then_28():
    assert get_human_age(56, 78) == [10, 12]
