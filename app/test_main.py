import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "age_of_cat,age_of_dog,expected",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (40, 40, [6, 5])
    ]
)
def test_get_human_age(age_of_cat: int,
                       age_of_dog: int,
                       expected: list) -> None:
    assert(get_human_age(age_of_cat, age_of_dog)
           == expected), f"Expected result = {expected}"
