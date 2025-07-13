import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (100, 100, [21, 17]),
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),

    ]
)
def test_cat_dog_years_to_human(cat_age: int,
                                dog_age: int, expected: list[int]) -> None:

    assert get_human_age(cat_age, dog_age) == expected
