from app.main import get_human_age


def test_bottom_boundary_zero_year() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_top_boundary_zero_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_bottom_boundary_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_top_boundary_first_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_bottom_boundary_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_top_boundary_second_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_age_less_dog_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_cat_age_more_dog_year() -> None:
    assert get_human_age(100, 100) == [21, 17]
