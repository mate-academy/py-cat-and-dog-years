from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_ages_below_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_ages_at_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_ages_within_second_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_ages_at_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_ages_within_third_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_ages_at_third_year_dog_diff() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_cat_age_only() -> None:
    assert get_human_age(30, 0) == [3, 0]


def test_dog_age_only() -> None:
    assert get_human_age(0, 30) == [0, 3]


def test_unequal_ages() -> None:
    assert get_human_age(50, 70) == [8, 11]


def test_cat_edge_case() -> None:
    assert get_human_age(28, 0) == [3, 0]


def test_dog_edge_case() -> None:
    assert get_human_age(0, 29) == [0, 3]
