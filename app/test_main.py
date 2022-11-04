import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
    ],
    ids=[
        "Up to 15 cat/dog years give 0 human year",
        "First 15 cat/dog years give 1 human year",
        "24 cat/dog years should be equal 1 human years",
        "Every 4 next cat years give 1 extra human year",
        "Every 5 next dog years give 1 extra human year.",
        "28 cat years should be equal 3 human years",
        "29 dog years should be equal 3 human years",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_age: list) -> None:
    assert (
            get_human_age(cat_age, dog_age) == human_age
    ), f"Cat years: {cat_age} and Dog years: {dog_age} should be equal to human years: {human_age}"
