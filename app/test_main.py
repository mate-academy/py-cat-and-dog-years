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
        (29, 29, [3, 3]),
    ],
    ids=[
        "0 cat/dog years → 0 human years",
        "14 cat/dog years → 0 human years",
        "15 cat/dog years → 1 human year",
        "23 cat/dog years → 1 human year",
        "24 cat/dog years → 2 human years",
        "27 cat/dog years → 2 human years",
        "28 cat years → 3, 27 dog years → 2",
        "29 cat years → 3, 29 dog years → 3",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
