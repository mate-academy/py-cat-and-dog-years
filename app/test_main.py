import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        (0, 0, [0, 0]),
        (14, 9, [0, 0]),
        (15, 9, [1, 0]),
        (20, 15, [1, 1]),
        (25, 24, [2, 2]),
        (29, 30, [3, 3]),
        (30, 50, [3, 7]),
        (35, 80, [4, 13]),
        (40, 100, [6, 17]),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age
