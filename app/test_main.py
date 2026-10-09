import app.main

def test_zero_years() -> None:
    assert app.main.get_human_age(0, 0) == [0, 0]

def test_boundary_before_first_human_year() -> None:
    assert app.main.get_human_age(14, 14) == [0, 0]

def test_boundary_exactly_first_human_year() -> None:
    assert app.main.get_human_age(15, 15) == [1, 1]

def test_boundary_before_second_human_year() -> None:
    assert app.main.get_human_age(23, 23) == [1, 1]

def test_boundary_exactly_second_human_year() -> None:
    assert app.main.get_human_age(24, 24) == [2, 2]

def test_boundary_before_third_human_year() -> None:
    # Cat hits 3rd year at 28, Dog hits 3rd year at 29
    assert app.main.get_human_age(27, 27) == [2, 2]
    assert app.main.get_human_age(27, 28) == [2, 2]

def test_boundary_exactly_third_human_year_for_cat() -> None:
    assert app.main.get_human_age(28, 28) == [3, 2]

def test_boundary_exactly_third_human_year_for_dog() -> None:
    assert app.main.get_human_age(28, 29) == [3, 3]

def test_large_numbers() -> None:
    assert app.main.get_human_age(100, 100) == [21, 17]

def test_different_ages_for_animals() -> None:
    assert app.main.get_human_age(100, 14) == [21, 0]
    assert app.main.get_human_age(14, 100) == [0, 17]
