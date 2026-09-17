from app import main
import pytest


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
        (29, 29, [3, 3]),
        (28, 14, [3, 0]),
        (14, 29, [0, 3]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected_result
