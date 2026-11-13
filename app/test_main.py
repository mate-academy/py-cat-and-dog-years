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
        (1, 2, [0, 0]),
        (16, 17, [1, 1]),
        (31, 33, [3, 3]),
        (32, 34, [4, 4]),
        (36, 39, [5, 5]),
        (40, 40, [6, 5]),
        (50, 60, [8, 9]),
        (28, 24, [3, 2]),
        (24, 29, [2, 3]),
        (100, 15, [21, 1]),
        (15, 100, [1, 17]),
        (1, 100, [0, 17]),
        (100, 1, [21, 0]),
        (1000, 1000, [246, 197]),
        (10000, 10000, [2496, 1997]),
        (-1, -1, [0, 0]),
        (-100, 20, [0, 1]),
        (20, -100, [1, 0]),
    ]
)
def test_get_human_age_expected_results(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("invalid", 20),
        (20, "invalid"),
        (None, 20),
        (20, None),
        ([], 20),
        (20, []),
    ]
)
def test_get_human_age_invalid_types(
    cat_age: object,
    dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


def test_get_human_age_returns_list() -> None:
    result = get_human_age(29, 30)
    assert isinstance(result, list)


def test_get_human_age_returns_two_elements() -> None:
    result = get_human_age(33, 35)
    assert len(result) == 2


def test_get_human_age_returns_integers() -> None:
    result = get_human_age(42, 46)
    assert all(isinstance(age, int) for age in result)
