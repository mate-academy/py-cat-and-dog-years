import pytest

import app.main as main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


def test_get_human_age_should_raise_error_with_string() -> None:
    with pytest.raises(TypeError):
        main.get_human_age("15", 15)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 15),
        (15, -1),
        (101, 15),
        (15, 101),
        (4000, 4000),
    ],
)
def test_check_if_age_is_unreal(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)
