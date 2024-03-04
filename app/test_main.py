import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
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
       "Test of current age, first 15 cat years give 1 human year",
       "Test of current age, first 15 cat years give 1 human year",
       "Test of current age, the next 9 cat years give 1 more human year",
       "Test of current age, the next 9 cat years give 1 more human year",
       "Test of current age, the next 9 cat years give 1 more human year",
       "Test of current age, every 4 next cat years give 1 extra human year",
       "Test of current age, every 4 next cat years give 1 extra human year",
       "Test of current age, every 4 next cat years give 1 extra human year"

    ]
)
def test_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        ("15", 15, TypeError),
        (15, "15", TypeError),
    ],
    ids=[
        "cat_age should be int!",
        "dog_age should be int!",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, error: TypeError) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
