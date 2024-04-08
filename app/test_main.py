import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "Should return [0, 0]",
        "if age is less 15",
        "if age is equal 15",
        "if age is equal 23",
        "if age is equal 24",
        "if age is equal 27",
        "If age is over 24",
        "Big numbers",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age
