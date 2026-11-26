import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (32, 34, [4, 4]),
        (100, 100, [21, 17]),
    ],
)
def test_should_convert_cat_and_dog_years_to_human_years(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-1, -1),
        (-100, 10),
        (10, -100),
    ],
)
def test_should_raise_value_error_for_negative_age(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.0, 15),
        (15, 15.0),
        (None, 15),
        (15, None),
    ],
)
def test_should_raise_type_error_for_incorrect_type(
        cat_age: object,
        dog_age: object
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (0, 0),
        (28, 29),
        (100, 100),
    ],
)
def test_should_return_two_integer_values(
        cat_age: int,
        dog_age: int
) -> None:
    result = main.get_human_age(cat_age, dog_age)

    assert len(result) == 2
    assert all(type(age) is int for age in result)
