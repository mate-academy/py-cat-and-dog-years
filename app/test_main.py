import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (28, 29, [3, 3]),
        (30, 30, [3, 3]),
        (28, 28, [3, 2]),
        (27, 29, [2, 3]),
        (100, 100, [21, 17]),
        (-15, -15, [0, 0])
    ], ids=[
        "should return zero if cat/dog age is zero",
        "should return zero if ages < 15",
        "should return 1 if ages = 15",
        "should return 1 if ages > 15",
        "should return 2 if year = 24",
        "should return 2 if year > 24",
        "should return 3 if cat's/dog's year = 28/29",
        "should return 3 if cat's/dog's year > 28/29",
        "should return different ages if cat's and dog's year = 28",
        "should return different ages if cat's/dog's year = 27/29",
        "should return result for large number of ages",
        "should return 0 for negative ages"
    ]
)
def test_get_human_age_correctly(
        cat_age: int,
        dog_age: int,
        human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
