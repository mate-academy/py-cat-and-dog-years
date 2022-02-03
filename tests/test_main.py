import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    'cat_age, dog_age, expected',
    [
        (-25, 23, [0, 1]),
        (23, -100, [1, 0]),
        (-1, -1, [0, 0])
    ]
)
def test_when_cat_age_or_dog_age_is_negative(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    'cat_age, dog_age, expected',
    [
        (100, 100, [21, 17]),
        (200, 200, [46, 37]),
        (333, 222, [79, 41])
    ]
)
def test_for_large_years_cat_and_dog(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    'cat_age, dog_age, expected',
    [
        (15, 15, [1, 1]),
        (26, 27, [2, 2]),
        (56, 52, [10, 7]),
        (0, 0, [0, 0])
    ]
)
def test_for_small_years_cat_and_dog(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
