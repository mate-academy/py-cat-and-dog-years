from app.main import get_human_age


def test_check_age_below_fifteen():
    assert get_human_age(14, 14) == [0, 0]


def test_test_check_first_year():
    assert get_human_age(15, 15) == [1, 1]


def test_check_human_age_after_first_year():
    assert get_human_age(28, 28) == [3, 2]
