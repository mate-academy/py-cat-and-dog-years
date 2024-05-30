import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),  # test should return zero age
        (14, 14, [0, 0]),  # test should return animals have not a year
        (23, 23, [1, 1]),  # test should return animals have one year
        (27, 27, [2, 2]),  # test should return animals have two years
        (28, 28, [3, 2]),  # test should return animal have different age
        (100, 100, [21, 17]),  # test should return animals have 100 years
        (-2, -5, [0, 0]),  # test should return if animal have negative age
    ]
)
def test_modify(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
