from app.main import get_human_age


def test_should_return_right_value():
    result = get_human_age(15, 15)
    assert result == [1, 1]


def test_when_ages_zero():
    result = get_human_age(0, 0)
    assert result == [0, 0]


def test_when_one_age_zero():
    result = get_human_age(15, 0)
    assert result == [1, 0]


def test_third_human_year():
    result = get_human_age(28, 28)
    assert result == [3, 2]


def test_several_cycle_iteration():
    result = get_human_age(100, 100)
    assert result == [21, 17]
