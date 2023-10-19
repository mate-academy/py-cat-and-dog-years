import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_list",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-10, -10, [0, 0]),
    ]
)
def test_counting_dog_ang_cat_years(cat_age: int,
                                    dog_age: int,
                                    expected_list: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_list


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ([], []),
        ("x", "b"),
        ({}, {})
    ]
)
def test_unsupported_types_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
