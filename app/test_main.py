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
        (100, 100, [21, 17]),
    ]
)
def test_examples_from_task(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_age_grows_every_4_years_after_24():
    assert get_human_age(28, 0)[0] == get_human_age(24, 0)[0] + 1
    assert get_human_age(40, 0)[0] == get_human_age(36, 0)[0] + 1


def test_dog_age_grows_every_5_years_after_24():
    assert get_human_age(29, 0)[1] == get_human_age(24, 0)[1]
    assert get_human_age(30, 0)[1] == get_human_age(24, 0)[1] + 1


def test_cat_and_dog_are_calculated_independently():
    assert get_human_age(28, 10)[1] == get_human_age(24, 10)[1]
    assert get_human_age(10, 30)[0] == get_human_age(10, 24)[0]