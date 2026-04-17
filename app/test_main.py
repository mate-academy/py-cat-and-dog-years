import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero_ages",
        "below_first_threshold",
        "first_threshold",
        "above_first_threshold",
        "below_second_threshold",
        "second_threshold",
        "mixed_ages",
        "large_ages"
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("23", 23),
        (23, "23"),
        (23.5, 23),
        (23, 23.5),
        (None, 23),
    ],
)
def test_invalid_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1),
        (-5, -5),
    ],
)
def test_negative_values(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
