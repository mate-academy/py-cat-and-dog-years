from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (15, -1, [1, 0]),
        (-1, 15, [0, 1]),
        (-2, -3, [0, 0]),
        (250, 300, [58, 57])
    ]
)
def test_get_human_age_valid(
        cat_age: int,
        dog_age: int,
        expected_result: int
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
