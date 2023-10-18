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
        (100, 100, [21, 17])
    ],
    ids=[
        "0, 0 as an input",
        "14, 14 as an input",
        "15, 15 as an input",
        "23, 23 as an input",
        "24, 24 as an input",
        "27, 27 as an input",
        "28, 28 as an input",
        "100, 100 as an input",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), f"{cat_age} and {dog_age} as an input should give {result}"
