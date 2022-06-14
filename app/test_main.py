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


def test_human_age_when_animal_age_is_huge():
    age = get_human_age(100, 100)
    assert age == [21, 17]


def test_human_age_when_animal_age_is_zero():
    age = get_human_age(0, 0)
    assert age == [0, 0]


def test_human_age_when_animal_age_is_negative():
    age = get_human_age(-1, -1)
    assert age == [0, 0]
