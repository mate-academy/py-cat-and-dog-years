import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (5, 5, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
    ]
)
def test_get_human_age_pet_positive(cat_age: int,
                                    dog_age: int,
                                    expected: int) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (28, 28, [3, 2]),
        (17, 29, [1, 3]),
        (29, 6, [3, 0]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_pet_independent(cat_age: int,
                                       dog_age: int,
                                       expected: int) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected
