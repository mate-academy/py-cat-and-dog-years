import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result", [
        (-1, -2, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (5000, 9999, [1246, 1997])
    ])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result", [
        ("cat", 2, TypeError),
        (0, "", TypeError),
        ("44", "55", TypeError),
        (None, 44, TypeError),
        ([23], 23, TypeError),
        ({24: ["2", "3"]}, 24, TypeError),
        (10, (2, 3), TypeError),
    ])
def test_str_types(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
