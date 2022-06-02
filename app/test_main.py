from app.main import get_human_age


def test_before_15():
    assert get_human_age(12, 12) == [0, 0]


def test_15():
    assert get_human_age(15, 15) == [1, 1]


def test_cat_from_24():
    assert get_human_age(25, 0)[0] == 2


def test_dog_from_24():
    assert get_human_age(0, 26)[1] == 2
