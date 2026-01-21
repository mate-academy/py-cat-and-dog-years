import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
    ]
)
def test_should_return_zero_for_age_below_15(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
    ]
)
def test_should_return_one_for_age_between_15_and_23(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
    ]
)
def test_should_return_two_for_age_between_24_and_27(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (28, 28, [3, 2]),
    ]
)
def test_should_return_different_ages_for_28_years(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (100, 100, [21, 17]),
    ]
)
def test_should_return_correct_age_for_large_values(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
