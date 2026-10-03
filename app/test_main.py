import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
    ],
)
def test_age_below_first_threshold_gives_zero_human_years(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
    ],
)
def test_age_in_second_range_gives_one_human_year(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_age_at_second_threshold_gives_two_human_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_age_just_below_cat_extra_rate_still_two_human_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_reaches_first_extra_year_at_rate_of_four() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_dog_reaches_first_extra_year_at_rate_of_five() -> None:
    assert get_human_age(29, 29) == [3, 3]


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (100, 100, [21, 17]),
    ],
)
def test_large_age_values(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_and_dog_have_different_extra_years_rate() -> None:
    result = get_human_age(28, 28)
    assert result[0] != result[1]
