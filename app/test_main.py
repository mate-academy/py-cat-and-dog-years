from app import main
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (10, 14, [0, 0]),
        (15, 15, [1, 1]),
        (28, 28, [3, 2]),
        (24, 24, [2, 2]),
        (23, 23, [1, 1]),
        (100, 100, [21, 17]),
        (0, 0, [0, 0]),
        (31, 31, [3, 3]),
        (32, 32, [4, 3])
    ],
    ids={
        "should return zero human years when age is less than 15",
        "first 15 cat and dog years give 1 human year",
        "cat and dog should have different human age",
        "24 is the second human age",
        "23 is still the first human age",
        "100 years should return correct human years",
        "should return 0 human years when age is 0",
        "should return 0 human years when age is 14",
        "should return 2 human years when age is 27"
    }
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected
