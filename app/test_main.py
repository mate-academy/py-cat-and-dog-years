import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 27, [1, 2]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_calculate_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-1, -1, [0, 0]),
        (-10, 5, [0, 0]),
        (5, -10, [0, 0]),
        (
            1000,
            1000,
            [2 + (1000 - 24) // 4, 2 + (1000 - 24) // 5],
        ),
        (
            10000,
            20000,
            [2 + (10000 - 24) // 4, 2 + (20000 - 24) // 5],
        ),
    ],
)
def test_large_and_negative(
    cat_age: int,
    dog_age: int,
    result: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 10),
        (10, "20"),
        (None, 10),
        (10, None),
        (10.5, 20),
    ],
)
def test_invalid_types(cat_age: object, dog_age: object) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
