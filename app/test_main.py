import pytest
from app import main


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (28, 29, [3, 3]),
    (100, 100, [21, 17]),
])
def test_get_human_age_returns_correct_result(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age", [
    (0, 1), (3, 6), (15, 16),
])
def test_get_human_age_returns_list_of_two_elements(
    cat_age: int,
    dog_age: int
) -> None:
    result = main.get_human_age(cat_age, dog_age)
    assert len(result) == 2


@pytest.mark.parametrize("cat_age, dog_age", [
    (0, 34), (10, 15), (-4, 100),
])
def test_get_human_age_returns_integers(
    cat_age: int,
    dog_age: int
) -> None:
    result = main.get_human_age(cat_age, dog_age)
    assert all(isinstance(age, int) for age in result)
