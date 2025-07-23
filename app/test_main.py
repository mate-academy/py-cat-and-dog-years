import pytest
from app.main import get_human_age, convert_to_human


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(cat_age: float, dog_age: float,
                       expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "years,first,second,each,expected",
    [
        (14, 15, 9, 4, 0),
        (15, 15, 9, 4, 1),
        (23, 15, 9, 4, 1),
        (24, 15, 9, 4, 2),
        (28, 15, 9, 4, 3),
    ]
)
def test_convert_to_human(years, first, second, each, expected):
    assert convert_to_human(years, first, second, each) == expected
