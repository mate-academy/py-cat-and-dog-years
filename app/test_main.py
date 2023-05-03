from app.main import get_human_age

# fifteen is the age of both cat and dog turn 1 year old
# twenty-four is the age of both cat and dog turn 2 years old
# twenty-eight is the age of cat turns 3 years old and dog still 2 years old


def test_edge_case_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_one_year_old() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_one_year_old() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_less_than_two_years_old() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_two_years_old() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_less_than_three_years_old() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_three_for_cat_and_still_two_for_dog_years_old() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_edge_case_hundred() -> None:
    assert get_human_age(100, 100) == [21, 17]
