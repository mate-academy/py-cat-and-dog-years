from app.main import get_human_age


def test_age_under_15():
    assert get_human_age(14, 13) == [0, 0]


def test_cat_age_15_to_23():
    assert get_human_age(23, 24)[0] == 1


def test_dog_age_15_to_23():
    assert get_human_age(26, 23)[1] == 1


def test_cat_age_after_24():
    assert get_human_age(36, 12)[0] == 5
    assert get_human_age(46, 16)[0] == 7
    assert get_human_age(269, 13)[0] == 63


def test_dog_age_after_24():
    assert get_human_age(22, 32)[1] == 3
    assert get_human_age(16, 25)[1] == 2
    assert get_human_age(18, 574)[1] == 112
