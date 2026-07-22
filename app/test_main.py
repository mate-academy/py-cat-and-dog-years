import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (0, 0),
        (14, 14)
    ]
)
def test_should_return_0_when_ages_are_less_than_15(
        cat_age: int,
        dog_age: int,
) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (15, 15),
        (23, 23)
    ]
)
def test_should_return_1_when_ages_are_between_15_and_23(
        cat_age: int,
        dog_age: int,
) -> None:
    assert get_human_age(cat_age, dog_age) == [1, 1]


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (24, 24),
        (27, 27)
    ]
)
def test_should_return_2_when_ages_are_between_24_and_27(
        cat_age: int,
        dog_age: int,
) -> None:
    assert get_human_age(cat_age, dog_age) == [2, 2]


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
    ]
)
def test_should_calculate_human_age_after_27_years(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_should_calculate_human_age_correctly_with_big_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
