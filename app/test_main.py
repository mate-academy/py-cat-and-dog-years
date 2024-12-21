import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-5, 0, [0, 0]),
        (15, 30, [1, 2]),
        (50, 50, [4, 4]),
        (1000, 1000, [209, 176]),
    ],
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
) -> None:
    result: list[int] = get_human_age(cat_age, dog_age)
    assert result == expected_result


def test_invalid_ages() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 10)

    with pytest.raises(ValueError):
        get_human_age(10, -1)

    with pytest.raises(ValueError):
        get_human_age(-1, -1)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (23, 23, [1, 1]),
    ],
)
def test_boundary_ages(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
) -> None:
    result: list[int] = get_human_age(cat_age, dog_age)
    assert result == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [(1000, 1000, [209, 176]), (5000, 5000, [990, 890])],
)
def test_large_ages(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
) -> None:
    result: list[int] = get_human_age(cat_age, dog_age)
    assert result == expected_result


def test_very_large_age() -> None:
    assert get_human_age(10**6, 10**6) == [209000, 176000]
