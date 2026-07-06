import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (32, 32, [4, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_valid_cases(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
    ],
)
def test_get_human_age_boundary_values(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, [0, 0]),
        (-100, -100, [0, 0]),
        (1000, 1000, [246, 197]),
    ],
)
def test_get_human_age_out_of_range_values(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (None, 15),
    ],
)
def test_get_human_age_invalid_type_raises_error(
    cat_age: int | str | float | None,
    dog_age: int | str | float | None,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
