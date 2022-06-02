from app.main import get_human_age


def test_age_before_15():
    assert get_human_age(12, 12) == [0, 0]


def test_age_before_23():
    assert get_human_age(22, 22) == [1, 1]


def test_age_after_24():
    assert get_human_age(24, 24) == [1, 1]
