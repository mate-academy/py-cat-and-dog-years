import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0]),
        (16, 10, [1, 0]),
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
    ],
    ids=[
        "both_0",
        "both_14",
        "both_15",
        "both_28",
        "both_100",
        "both_negative",
        "cat_16_dog_10",
        "cat_15_dog_0",
        "cat_0_dog_15",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
