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
    young_cat = get_human_age(36, 12)
    middle_cat = get_human_age(46, 16)
    very_old_cat = get_human_age(269, 13)

    assert young_cat[0] == 5
    assert middle_cat[0] == 7
    assert very_old_cat[0] == 63


def test_dog_age_after_24():
    middle_dog = get_human_age(22, 32)
    young_dog = get_human_age(16, 25)
    very_old_dog = get_human_age(18, 574)

    assert middle_dog[1] == 3
    assert young_dog[1] == 2
    assert very_old_dog[1] == 112
