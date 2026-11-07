import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_examples_from_task(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,expected",
    [
        (28, [3, 0]),
        (31, [3, 0]),
        (32, [4, 0]),
    ],
)
def test_cat_gets_extra_year_every_four_years(
    cat_age: int,
    expected: list
) -> None:
    assert main.get_human_age(cat_age, 0) == expected


@pytest.mark.parametrize(
    "dog_age,expected",
    [
        (28, [0, 2]),
        (29, [0, 3]),
        (33, [0, 3]),
        (34, [0, 4]),
    ],
)
def test_dog_gets_extra_year_every_five_years(
    dog_age: int,
    expected: list
) -> None:
    assert main.get_human_age(0, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 0),
        (0, -1),
        (-10, -10),
    ],
)
def test_negative_ages_should_raise_value_error(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 10),
        (10, "15"),
        (10.5, 10),
        (10, 10.5),
        (None, 10),
        ([15], 10),
    ],
)
def test_incorrect_types_should_raise_type_error(
    cat_age: object,
    dog_age: object
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
