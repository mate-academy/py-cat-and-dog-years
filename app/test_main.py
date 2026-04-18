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
        (32, 29, [4, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero_age",
        "less_than_15",
        "years_15",
        "between_15_24",
        "years_24",
        "after_24",
        "cat_vs_dog_step",
        "different_inputs",
        "large_numbers",
    ]
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
