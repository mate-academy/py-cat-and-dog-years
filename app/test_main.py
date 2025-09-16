from app.main import get_human_age


def test_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]

def test_years_post_first_animal_first_year() -> None:
    assert  get_human_age(14, 14) == [0, 0]

def test_years_first_animal_year() -> None:
    assert get_human_age(15, 15) == [1, 1]

def test_years_post_first_animal_second_year() -> None:
    assert get_human_age(23, 23) == [1, 1]

def test_years_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]

def test_years_last_time_together_two_years() -> None:
    assert get_human_age(27, 27) == [2, 2]

def test_years_firs_only_cat_third_year() -> None:
    assert get_human_age(28, 28) == [3, 2]

def test_years_100_years_old() -> None:
    assert get_human_age(100, 100) == [21, 17]
