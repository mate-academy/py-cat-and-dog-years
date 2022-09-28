from app.main import get_human_age


def test_zero_ages():
    result1 = get_human_age(15, 15)
    assert result1 == [1, 1]


def test_first_ages():
    result2 = get_human_age(24, 24)
    assert result2 == [2, 2]


def test_second_ages():
    result = get_human_age(28, 29)
    assert result == [3, 3]
