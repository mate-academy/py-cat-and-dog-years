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


def test_every_4_years_after_28_for_cat_should_add_a_year():
    goals = get_human_age(32, 29)

    assert goals == [4, 3]


def test_every_5_years_after_29_for_dog_should_add_a_year():
    goals = get_human_age(28, 39)

    assert goals == [3, 5]


def test_big_numbers_of_years():
    goals = get_human_age(100, 100)

    assert goals == [21, 17]
