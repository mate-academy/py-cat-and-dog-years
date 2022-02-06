from app.main import get_human_age


def test_age_under_15():
    goals = get_human_age(14, 13)

    assert goals[0] == 0


def test_cat_age_15_to_23():
    goals = get_human_age(23, 24)

    assert goals[0] == 1


def test_dog_age_15_to_23():
    goals = get_human_age(26, 23)

    assert goals[1] == 1


def test_cat_age_after_24():
    goals1 = get_human_age(36, 12)
    goals2 = get_human_age(46, 16)
    goals3 = get_human_age(269, 13)

    assert goals1[0] == 5
    assert goals2[0] == 7
    assert goals3[0] == 63


def test_dog_age_after_24():
    goals1 = get_human_age(22, 32)
    goals2 = get_human_age(16, 25)
    goals3 = get_human_age(18, 574)

    assert goals1[1] == 3
    assert goals2[1] == 2
    assert goals3[1] == 112
