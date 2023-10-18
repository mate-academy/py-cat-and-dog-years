import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "age_of_cat,age_of_dog,expected",
    [
        (-2, -2, [0, 0]),
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 29, [2, 3]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])

    ]
)
def test_get_human_age(age_of_cat: int, age_of_dog: int, expected: list) -> None:
    assert (get_human_age(age_of_cat, age_of_dog) == expected
            ), f"Expected result should = {expected}"


@pytest.mark.parametrize(
    "age_of_cat,age_of_dog",
    [
        ("1", 2),
        ([1], 2),
        ((1,), 2),
        ({1}, 2),
    ]
)
def test_check_incorrect_types(age_of_cat: int, age_of_dog: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(age_of_cat, age_of_dog)
