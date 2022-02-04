from app.main import get_human_age


def test_low_ages():
    assert get_human_age(0, 14) == [0, 0]


def test_one_human_year():
    assert get_human_age(15, 15) == [1, 1]


def test_cat_from_24_to_27():
    assert get_human_age(27, 28)[0] == 2


def test_dog_from_24_to_28():
    assert get_human_age(10, 28)[1] == 2


def test_great_age():
    assert get_human_age(100, 100) == [21, 17]
