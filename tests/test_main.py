from app.main import get_human_age


def test_zeros_animal_years():
    assert get_human_age(0, 0) == [0, 0]


def test_14_edge_first_year_years():
    assert get_human_age(14, 14) == [0, 0]


def test_15_edge_first_year_years():
    assert get_human_age(15, 15) == [1, 1]


def test_23_edge_second_year_years():
    assert get_human_age(23, 23) == [1, 1]


def test_24_edge_second_year_years():
    assert get_human_age(24, 24) == [2, 2]


def test_27_28_edge_third_years():
    assert get_human_age(27, 28) == [2, 2]


def test_28_29_edge_third_years():
    assert get_human_age(28, 29) == [3, 3]


def test_big_numbers():
    assert get_human_age(100, 100) == [21, 17]



