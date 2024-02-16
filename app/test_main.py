import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (1, -1, [0, 0]),
        (-1, 15, [0, 1]),
        (10, -99, [0, 0])
    ]
)
def test_when_cat_or_dog_age_is_negative(cat_age: int,
                                         dog_age: int,
                                         expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (100, 100, [21, 17]),
        (200, 200, [46, 37]),
        (333, 222, [79, 41])
    ]
)
def test_for_large_years_for_cat_and_dog(cat_age: int,
                                         dog_age: int,
                                         expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (1, 1, [0, 0]),
        (26, 15, [2, 1]),
        (56, 52, [10, 7])
    ]
)
def test_for_small_years_for_cat_and_dog(cat_age: int,
                                         dog_age: int,
                                         expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
