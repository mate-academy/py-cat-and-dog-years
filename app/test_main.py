from app.main import get_human_age


# If you're reviewing this code - thank you <3

def test_with_zero_parameters():
    assert get_human_age(0, 0) == [0, 0]


def test_get_zero_year():
    assert get_human_age(14, 14) == [0, 0]


def test_get_one_year():
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_get_two_years():
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 28) == [2, 2]


def test_get_three_years():
    assert get_human_age(28, 29) == [3, 3]


def test_with_large_number():
    assert get_human_age(100, 100) == [21, 17]
