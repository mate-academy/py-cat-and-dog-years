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
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (200, 200, ValueError),
        (-1, 10, ValueError),
        ("10", 10, TypeError),
        (None, 10, TypeError),
    ]
)
def test_get_human_age_conversion(cat_age: int,
                                  dog_age: int,
                                  expected: list[int]) -> None:
    if isinstance(expected, type):
        with pytest.raises(expected):
            get_human_age(cat_age, dog_age)
    else:
        assert get_human_age(cat_age, dog_age) == expected
