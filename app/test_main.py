from app.main import get_human_age


def test_should_return_zeros_when_animals_age_less_15():
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_one_when_animals_age_range_15_23():
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2():
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_3():
    assert get_human_age(28, 29) == [3, 3]


def test_big_ages():
    assert get_human_age(100, 100) == [21, 17]
