import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
])
def test_when_cat_and_dog_less_than_1_human_year(
        cat_age: int,
        dog_age: int,
        expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
])
def test_when_cat_and_dog_have_1_human_year(
        cat_age: int,
        dog_age: int,
        expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_cat_and_dog_are_more_than_2_years_old(
        cat_age: int,
        dog_age: int,
        expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    ("2", 3, ValueError),
    (2, "3", ValueError),
    (1.5, 3, ValueError),
    (2, 3.5, ValueError),
])
def test_cat_and_dog_age_are_not_string_or_float(
        cat_age: int,
        dog_age: int,
        expected: list or type) -> None:
    if isinstance(expected, list):
        assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (-1, 3, ValueError),
    (3, -1, ValueError),
])
def test_cat_and_dog_age_are_not_negative_values(
        cat_age: int,
        dog_age: int,
        expected: list or type) -> None:
    if isinstance(expected, list):
        assert get_human_age(cat_age, dog_age) == expected
