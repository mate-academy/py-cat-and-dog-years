import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,result",
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
        "function should return 0 if the age of the animals is 0",
        "function should return 0 if the age of the animals < 15",
        "function should return 1 if the age of the animals 15",
        "function should return 1 if the age of the animals < 24",
        "function should return 2 if the age of the animals 24",
        "function should return 2 if the age of the animals < 27",
        "function should correctly count the age of dogs and cats over 28",
        "function should correctly count the age of dogs and cats over 28"


    ]
)
def test_get_human_age(cat_years: int, dog_years: int, result: list) -> None:
    assert get_human_age(cat_years, dog_years) == result
