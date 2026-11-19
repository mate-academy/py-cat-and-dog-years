import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "both animals are 0 years old",
        "14 years is still 0 human years",
        "15 years is 1 human year",
        "23 years is still 1 human year",
        "24 years is 2 human years",
        "27 years is still 2 human years",
        "28 cat years is 3 human years but 28 dog years is 2",
        "29 cat and dog years are 3 human years",
        "100 cat and dog years",
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected
