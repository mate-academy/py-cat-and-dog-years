from app.main import get_human_age


def test_both_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0], "Expected [0, 0] for ages 0, 0"


def test_both_below_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0], "Expected [0, 0] for ages 14, 14"


def test_both_exact_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1], "Expected [1, 1] for ages 15, 15"


def test_both_above_first_year_but_below_second_year() -> None:
    assert get_human_age(23, 23) == [1, 1], "Expected [1, 1] for ages 23, 23"


def test_both_at_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2], "Expected [2, 2] for ages 24, 24"


def test_both_above_second_year() -> None:
    assert get_human_age(27, 27) == [2, 2], "Expected [2, 2] for ages 27, 27"


def test_cat_more_years_than_dog() -> None:
    assert get_human_age(28, 28) == [3, 2], "Expected [3, 2] for ages 28, 28"


def test_high_ages() -> None:
    assert get_human_age(100, 100) == [21, 17], (
        "Expected [21, 17] for ages 100, 100"
    )


def test_different_ages() -> None:
    assert get_human_age(30, 20) == [3, 1], "Expected [3, 1] for ages 30, 20"


def test_boundary_case() -> None:
    assert get_human_age(16, 16) == [1, 1], "Expected [1, 1] for ages 16, 16"
