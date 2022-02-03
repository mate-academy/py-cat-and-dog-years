from app.main import get_human_age


def test_age_should_be_positive_and_round():
    assert get_human_age(-1.1, -1.2) == [0, 0]
    assert get_human_age(5.1, 27.9) == [0, 2]
    assert get_human_age(15.01, 57.09) == [1, 8]
    assert get_human_age(55.001, 17.009) == [9, 1]


def test_age_on_first_human_year():
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_age_on_second_human_year():
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_age_on_more_two_human_years():
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(90, 40) == [18, 5]

