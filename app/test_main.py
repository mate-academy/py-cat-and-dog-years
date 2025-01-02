import pytest
from app.main import get_human_age


@pytest.mark.parametrize (
    "cat_age,dog_age,expected_human_age",
    [
        (9, 2, [0, 0]),
        (24, 29, [2, 3]),
        (14, 52, [0, 7]),
        (28, 15, [3, 1]),
        (23, 80, [1, 13])
    ]
)

def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_age: list
) -> None:
    assert(
        get_human_age(cat_age, dog_age) == expected_human_age
    )
