import pytest

from app.main import get_human_age


def test_when_age_of_animals_is_up_to_14_years():
    assert get_human_age(14, 14) == [0, 0]


def test_when_age_of_animals_is_up_to_23_years():
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_when_age_both_animals_is_negative():
    assert get_human_age(-3, -1) == [0, 0]


@pytest.mark.parametrize(
    'cat_age, dog_age, expected',
    [
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (72, 81, [14, 13]),
        (103, 103, [21, 17])
    ]
)
def test_age_of_animal_is_grater_than_23(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
