import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age: float, dog_age: float, expected: list",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23.99, 23.99, [1, 1]),
        (24, 24, [2, 2]),
        (27.99, 27.99, [2, 2]),
        (28, 28, [3, 2]),
        (29, 18, [3, 3]),
        (100, 100, [21, 17]),
        (46, 24, [6, 2]),
    ],
)
def test_get_human_age_edge_cases(cat_age: float, dog_age: float, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected