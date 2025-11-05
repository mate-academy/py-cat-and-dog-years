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
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_examples(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, expected_cat",
    [
        (0, 0),
        (15, 1),
        (24, 2),
        (28, 3),
        (32, 4),
        (36, 5),
        (40, 6),
        (100, 21),
    ],
)
def test_cat_conversion_only(cat_age: int, expected_cat: int) -> None:
    assert get_human_age(cat_age, 0)[0] == expected_cat


@pytest.mark.parametrize(
    "dog_age, expected_dog",
    [
        (0, 0),
        (15, 1),
        (24, 2),
        (29, 3),
        (34, 4),
        (39, 5),
        (44, 6),
        (100, 17),
    ],
)
def test_dog_conversion_only(dog_age: int, expected_dog: int) -> None:
    assert get_human_age(0, dog_age)[1] == expected_dog
