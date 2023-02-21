import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (150, 150, [33, 27])
    ]
)
def test_get_different_results_same_input(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    ), f"{cat_age} for cat and {dog_age} for dog should return {expected}"
