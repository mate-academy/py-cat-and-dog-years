import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (2, 2, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (10**6, 10**6, [249996, 199997]),
    ],
)
def test_valid_inputs(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_monotonicity() -> None:
    prev = get_human_age(0, 0)
    for years in range(1, 200):
        curr = get_human_age(years, years)
        assert curr[0] >= prev[0]
        assert curr[1] >= prev[1]
        prev = curr
