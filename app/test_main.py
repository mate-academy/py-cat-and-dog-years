import pytest

import app.main as main_module


@pytest.mark.parametrize("cat_age,dog_age,expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (25, 25, [2, 2]),
    (28, 0, [3, 0]),
    (0, 29, [0, 3]),
    (27, 0, [2, 0]),
    (0, 28, [0, 2]),
    (29, 29, [3, 3]),
    (100, 100, [21, 17]),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert main_module.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age,dog_age", [
    (-1, 0),
    (0, -1),
    (-5, -5),
])
def test_negative_ages_raise_value_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        main_module.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age,dog_age", [
    ("5", 0),
    (0, "5"),
    (1.5, 0),
    (0, 1.5),
    (None, 0),
    (0, None),
])
def test_invalid_types_raise_type_error(cat_age: any, dog_age: any) -> None:
    with pytest.raises(TypeError):
        main_module.get_human_age(cat_age, dog_age)
