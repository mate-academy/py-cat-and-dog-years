from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (0, -1, [0, None]),
        (-1, 0, [None, 0]),
        (15, -1, [1, None]),
        (-1, 15, [None, 1]),
        (-1, -1, [None, None]),
        (28, -1, [3, None]),
        (-1, 28, [None, 2])
    ],
    ids=[
        f"human age conversion for {0, 0}",
        f"human age conversion for {14, 14}",
        f"human age conversion for {15, 15}",
        f"human age conversion for {23, 23}",
        f"human age conversion for {24, 24}",
        f"human age conversion for {27, 27}",
        f"human age conversion for {28, 28}",
        f"human age conversion for {100, 100}",
        f"human age conversion for {0, -1}",
        f"human age conversion for {-1, 0}",
        f"human age conversion for {15, -1}",
        f"human age conversion for {-1, 15}",
        f"human age conversion for {-1, -1}",
        f"human age conversion for {28, -1}",
        f"human age conversion for {-1, 28}"
    ]
)
def test_human_age_conversion(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age, f"conversion should return {human_age}"


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (1.0, 0),
        (0.0, 1.0),
        (1.0, 1.0)
    ],
    ids=[
        f"expected error for {1.0, 0}",
        f"expected error for {0.0, 1.0}",
        f"expected error for {1.0, 1.0}"
    ]
)
def test_errro_if_parameters_are_not_int(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
