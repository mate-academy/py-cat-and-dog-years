from app.main import get_human_age


def test_dog_age_equal_to_zero():
    goals = get_human_age(0, 100)
    assert goals == [0, 17]

    goals = get_human_age(100, 0)
    assert goals == [21, 0]


def test_is_equal_to_human_one():
    goals = get_human_age(15, 15)
    assert goals == [1, 1]

    goals = get_human_age(23, 23)
    assert goals == [1, 1]


def test_is_equal_to_human_two():
    goals = get_human_age(24, 24)
    assert goals == [2, 2]

    goals = get_human_age(27, 27)
    assert goals == [2, 2]


def test_equal_animals_ages_different_human_ages():

    goals = get_human_age(28, 28)
    assert goals == [3, 2]
