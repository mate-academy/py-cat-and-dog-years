import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_ages",
    [
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (26, 0, [2, 0]),
        (0, 29, [0, 3]),
        (33, 35, [4, 4]),
        (40, 0, [6, 0]),
        (0, 45, [0, 6]),
        (48, 50, [8, 7]),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_ages: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_ages
