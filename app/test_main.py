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
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list[int]) \
        -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected, (
        f"Expected {expected} for cat_age {cat_age} and dog_age {dog_age}, "
        f"but got {result}."
    )
    result_unchanged = get_human_age(cat_age, dog_age)
    assert result == result_unchanged, (
        f"Expected the result to be unchanged for cat_age {cat_age} and "
        f"dog_age {dog_age}, but got a different value."
    )


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-5, -5),
        (1000, 1000)
    ]
)
def test_get_human_age_out_of_range(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == [0, 0], (
        f"Expected [0, 0] for out-of-range cat_age {cat_age} and dog_age {dog_age}, "
        f"but got {result}."
    )


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("fifteen", 15),
        (15, "fifteen"),
        (None, 15),
        (15, None),
        (15.5, 15),
        (15, 15.5)
    ]
)
def test_get_human_age_invalid_types(cat_age, dog_age) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
