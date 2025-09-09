import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (15, 24, [1, 2]),
        (28, 14, [3, 0]),
    ]
)
def test_get_human_age_base_and_asymmetric(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected
    assert all(isinstance(year, int) for year in result)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-3, -7),
    ],
)
def test_get_human_age_negatives(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert all(isinstance(year, int) for year in result)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (10 ** 6, 10 ** 6),
        (10 ** 9, 0),
        (0, 10 ** 9),
    ],
)
def test_get_human_age_large_values(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)
