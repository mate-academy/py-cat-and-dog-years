from app.main import get_human_age


def test_cat_age_converted_to_human_age_correctly():
    assert get_human_age(0, 10) == [0, 0]
    assert get_human_age(14, 10) == [0, 0]
    assert get_human_age(15, 10) == [1, 0]
    assert get_human_age(23, 10) == [1, 0]
    assert get_human_age(24, 10) == [2, 0]
    assert get_human_age(27, 10) == [2, 0]
    assert get_human_age(28, 10) == [3, 0]
    assert get_human_age(100, 10) == [21, 0]


def test_dog_age_converted_to_human_age_correctly():
    assert get_human_age(10, 0) == [0, 0]
    assert get_human_age(10, 14) == [0, 0]
    assert get_human_age(10, 15) == [0, 1]
    assert get_human_age(10, 23) == [0, 1]
    assert get_human_age(10, 24) == [0, 2]
    assert get_human_age(10, 28) == [0, 2]
    assert get_human_age(10, 29) == [0, 3]
    assert get_human_age(10, 100) == [0, 17]
