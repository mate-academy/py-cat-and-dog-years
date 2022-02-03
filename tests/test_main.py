import pytest

from app.main import get_human_age


def test_when_age_animals_until_14_years():
    assert get_human_age(14, 14) == [0, 0]


def test_when_age_animals_until_23_years():
    assert get_human_age(23, 23) == [1, 1]


def test_when_age_both_animals_is_negative():
    assert get_human_age(-3, -1) == [0, 0]


@pytest.mark.parametrize(
    'cat_age, dog_age, expected',
    [
        (27, 27, [2, 2]),
        (23, 30, [1, 3]),
        (72, 81, [14, 13]),
        (103, 103, [21, 17])
    ]
)
def test_mix_age_animals_after_23_years(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
