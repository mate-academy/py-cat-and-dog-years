def test_get_human_age_for_zero_years() -> None:
    from app.main import get_human_age
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_before_first_human_year() -> None:
    from app.main import get_human_age
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_exactly_first_human_year() -> None:
    from app.main import get_human_age
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_before_second_human_year() -> None:
    from app.main import get_human_age
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_exactly_second_human_year() -> None:
    from app.main import get_human_age
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_before_next_extra_year() -> None:
    from app.main import get_human_age
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_cat_gets_year_father_than_dog() -> None:
    from app.main import get_human_age
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_for_large_number() -> None:
    from app.main import get_human_age
    assert get_human_age(100, 100) == [21, 17]
