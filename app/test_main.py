import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (-1, -1, [0, 0]),
    (100, 100, [21, 17])
])
def test_get_human_age_with_param_deco(cat_age: int,
                                       dog_age: int,
                                       expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result, (
        f"Function 'get_human_age' should return {expected_result}"
        f"when value is Cat: {cat_age}, Dog: {dog_age}"
    )


@pytest.mark.parametrize("cat_age, dog_age, expected_errors", [
    ([], [], TypeError),
    ((), (), TypeError),
    ("", "", TypeError),
    ({}, {}, TypeError)])
def test_get_human_age_with_param_error(cat_age: int,
                                        dog_age: int,
                                        expected_errors: list) -> None:
    with pytest.raises(expected_errors):
        get_human_age(cat_age, dog_age)
