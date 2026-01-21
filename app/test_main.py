import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, cat_convert_age", [
    (-15, 0),
    (14, 0),
    (15, 1),
    (23, 1),
    (24, 2),
    (27, 2),
    (28, 3),
    (100, 21)
])
def test_cat_age_are_converted_to_human_years(
        cat_age: int,
        cat_convert_age: int
) -> None:
    goals = get_human_age(cat_age, 5)
    assert goals[0] == cat_convert_age


@pytest.mark.parametrize("dog_age, dog_convert_age", [
    (-15, 0),
    (14, 0),
    (15, 1),
    (23, 1),
    (24, 2),
    (28, 2),
    (29, 3),
    (100, 17)
])
def test_dog_age_are_converted_to_human_years(
        dog_age: int,
        dog_convert_age: int
) -> None:
    goals = get_human_age(5, dog_age)
    assert goals[1] == dog_convert_age
