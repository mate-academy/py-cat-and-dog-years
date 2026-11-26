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
        (100, 100, [21, 17]),
    ]
)
def test_should_return_expected_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, expected_cat_age",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
        (31, 3),
        (32, 4),
        (100, 21),
    ]
)
def test_should_convert_cat_age_correctly(
        cat_age: int,
        expected_cat_age: int
) -> None:
    result = main.get_human_age(cat_age, 0)

    assert result[0] == expected_cat_age


@pytest.mark.parametrize(
    "dog_age, expected_dog_age",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (28, 2),
        (29, 3),
        (33, 3),
        (34, 4),
        (100, 17),
    ]
)
def test_should_convert_dog_age_correctly(
        dog_age: int,
        expected_dog_age: int
) -> None:
    result = main.get_human_age(0, dog_age)

    assert result[1] == expected_dog_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (0, 0),
        (15, 15),
        (24, 24),
        (28, 29),
        (100, 100),
    ]
)
def test_should_return_two_integer_values(
        cat_age: int,
        dog_age: int
) -> None:
    result = main.get_human_age(cat_age, dog_age)

    assert len(result) == 2
    assert all(type(age) is int for age in result)
