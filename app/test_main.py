import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "should return [0, 0] at (0, 0)",
        "should return [0, 0] at (14, 14)",
        "should return [1, 1] at (15, 15)",
        "should return [1, 1] at (23, 23)",
        "should return [2, 2] at (24, 24)",
        "should return [2, 2] at (27, 27)",
        "should return [3, 2] at (28, 28)",
        "should return [21, 17] at (100, 100)"
    ]
)
def test_app(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
