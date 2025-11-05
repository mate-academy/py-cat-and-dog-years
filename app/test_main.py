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
        (32, 34, [4, 4]),
        (36, 39, [5, 5]),
        (40, 44, [6, 6]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_examples(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, [0, 0]),
        (-15, 0, [0, 0]),
        (0, -5, [0, 0]),
    ],
)
def test_negative_inputs(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.0, 15),
        (15, 15.0),
        ([15], 15),
        (15, {"age": 15}),
    ],
)
def test_invalid_types(
    cat_age: object,
    dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)  # type: ignore