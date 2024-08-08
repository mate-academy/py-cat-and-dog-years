from app.main import get_human_age


def test_get_human_age_zero():
    assert (
            get_human_age(0, 0) == [0, 0]
    ), "Test should return [0, 0] if both ages equals zero"


def test_get_human_age_less_than_first_year():
    assert (
            get_human_age(14, 14) == [0, 0]
    ), "Test should return [0, 0] if both of ages less than 15"


def test_get_human_age_exactly_first_year():
    assert (
            get_human_age(15, 15) == [1, 1]
    ), "Test should return [1, 1] if 15 <= both of ages <= 23"


def test_get_human_age_exactly_second_year():
    assert (
            get_human_age(24, 24) == [2, 2]
    ), "Test should return [2, 2] if 24 <= cat_age <= 27 and 24 <= dog_age <= 28"


def test_get_human_age_extra_years_for_cat():
    assert (
            get_human_age(28, 28) == [3, 2]
    ), "Test should return extra year for cat"
