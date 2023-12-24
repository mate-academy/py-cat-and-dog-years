from app.main import get_human_age


def test_age_15_15():
    assert get_human_age(15, 15) == [1, 1]


def test_age_24_24():
    assert get_human_age(24, 24) == [2, 2]


def test_age_28_29():
    assert get_human_age(28, 29) == [3, 3]
