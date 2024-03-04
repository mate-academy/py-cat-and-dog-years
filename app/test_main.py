from app.main import get_human_age


def test_how_old_is_14_years_old_pet() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_how_old_is_15_years_old_pet() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_how_old_is_23_years_old_pet() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_how_old_is_24_years_old_pet() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_how_old_is_27_years_old_cat_and_28_years_old_dog() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_how_old_is_28_years_old_cat_and_29_years_old_dog() -> None:
    assert get_human_age(28, 29) == [3, 3]
