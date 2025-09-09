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
        (31, 28, [3, 2]),
        (32, 29, [4, 3]),
        (35, 33, [4, 3]),
        (36, 34, [5, 4]),
        (39, 38, [5, 4]),
        (40, 39, [6, 5]),
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
    "cat_age, dog_age, expected",
    [
        (-1, 10, [0, 0]),
        (10, -5, [0, 0]),
        (-3, -7, [0, 0]),
    ]
)
def test_get_human_age_negatives(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(year, int) for year in result)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (10 ** 6, 10 ** 6, [249996, 199997]),
        (10 ** 9, 0, [249999996, 0]),
        (0, 10 ** 9, [0, 199999997]),
    ]
)
def test_get_human_age_large_values(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
