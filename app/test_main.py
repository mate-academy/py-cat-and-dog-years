from app.main import get_human_age


def test_zero_ages():
    age = get_human_age(14, 14)
    assert age == [0, 0]


def test_first_ages():
    age = get_human_age(15, 15)
    assert age == [1, 1]


def test_second_ages():
    age = get_human_age(28, 29)
    assert age == [3, 3]
