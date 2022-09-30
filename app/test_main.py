from app.main import get_human_age


def test_should_return_0_if_age_less_than_15():
    goals = get_human_age(0, 14)

    assert goals == [0, 0]


def test_should_return_1_if_age_more_than_14_and_less_24():
    goals = get_human_age(15, 23)

    assert goals == [1, 1]


def test_should_return_2_if_age_more_than_23_and_less_28():
    goals = get_human_age(24, 27)

    assert goals == [2, 2]


def test_should_return_3_if_age_more_than_27_for_cat_and_28_for_dog():
    goals = get_human_age(28, 29)

    assert goals == [3, 3]
