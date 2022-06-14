from app.main import get_human_age


def test_human_age_should_be_zero():
    age = get_human_age(14, 14)
    assert age == [0, 0]


def test_human_age_should_be_one():
    age = get_human_age(15, 15)
    assert age == [1, 1]


def test_human_age_should_be_three():
    age = get_human_age(28, 29)
    assert age == [3, 3]
