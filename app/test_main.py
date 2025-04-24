from app.main import get_human_age


def test_animal_age_0_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_animal_age_almost_1_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_animal_age_1_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_animal_age_almost_2_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_animal_age_2_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_animal_age_almost_3_years() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_animal_age_3_years() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_animal_each_years() -> None:
    assert get_human_age(36, 39) == [5, 5]


def test_minus_age() -> None:
    assert get_human_age(-1, -1) == [0, 0]


def test_old_cat_small_dog() -> None:
    assert get_human_age(36, 5) == [5, 0]
