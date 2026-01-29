import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (10.1, 2),
        (17, "6")
    ]
)
def test_with_invalid_types(
    cat_age: str | float,
    dog_age: str | float
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (150, 10),
        (17, 135)
    ]
)
def test_with_crazy_ages(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-15, 10),
        (17, -1)
    ]
)
def test_with_negative_ages(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (2, 8, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (31, 33, [3, 3]),
        (32, 34, [4, 4]),
        (100, 100, [21, 17])
    ]
)
def test_ages_are_calculated_correctly(
    cat_age: int,
    dog_age: int,
    result: list[int]
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), f"Failed: calculation incorrect, input {cat_age}, {dog_age}"
