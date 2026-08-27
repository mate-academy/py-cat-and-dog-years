import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
        (100, 21),
    ],
)
def test_cat_age(cat_age, expected):
    assert get_human_age(cat_age, 0)[0] == expected


@pytest.mark.parametrize(
    "dog_age, expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (28, 2),
        (29, 3),
        (100, 17),
    ],
)
def test_dog_age(dog_age, expected):
    assert get_human_age(0, dog_age)[1] == expected