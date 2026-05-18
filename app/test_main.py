import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
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
    ],
    ids=[
        "zero years",
        "14 years is still 0 human years",
        "15 years is 1 human year",
        "23 years is still 1 human year",
        "24 years is 2 human years",
        "27 years is still 2 human years",
        "28 cat and dog years differ",
        "29 years both reach 3 human years",
        "large age",
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,expected_cat_human_age",
    [
        (-1, 0),
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
    ],
)
def test_cat_age_boundaries(cat_age: int, expected_cat_human_age: int) -> None:
    result = get_human_age(cat_age, 0)
    assert result[0] == expected_cat_human_age
    assert result[1] == 0


@pytest.mark.parametrize(
    "dog_age,expected_dog_human_age",
    [
        (-1, 0),
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 2),
        (29, 3),
    ],
)
def test_dog_age_boundaries(dog_age: int, expected_dog_human_age: int) -> None:
    result = get_human_age(0, dog_age)
    assert result[0] == 0
    assert result[1] == expected_dog_human_age
