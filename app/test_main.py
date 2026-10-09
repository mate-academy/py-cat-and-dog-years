import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (0, 0),
        (1, 1),
        (14, 14),
        (0, 14),
        (14, 0),
    ],
)
def test_should_return_zero_when_ages_are_less_than_15(
    cat_age: int,
    dog_age: int,
) -> None:
    assert main.get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (15, 15),
        (20, 20),
        (23, 23),
        (15, 23),
        (23, 15),
    ],
)
def test_should_return_one_when_ages_are_from_15_to_23(
    cat_age: int,
    dog_age: int,
) -> None:
    assert main.get_human_age(cat_age, dog_age) == [1, 1]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (24, 24),
        (26, 26),
        (27, 27),
        (24, 28),
        (27, 24),
    ],
)
def test_should_return_two_when_ages_are_from_24_to_27(
    cat_age: int,
    dog_age: int,
) -> None:
    assert main.get_human_age(cat_age, dog_age) == [2, 2]


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (32, 33, [4, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_should_add_one_per_four_cat_years_and_five_dog_years(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 15, [0, 1]),
        (15, 14, [1, 0]),
        (23, 24, [1, 2]),
        (24, 23, [2, 1]),
    ],
)
def test_should_calculate_cat_and_dog_ages_independently(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, -1),
        (-100, 0),
        (0, -5),
    ],
)
def test_should_return_zeros_when_ages_are_negative(
    cat_age: int,
    dog_age: int,
) -> None:
    assert main.get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("abc", 1),
        (1, "abc"),
        ("15", 15),
        (15, "15"),
        (None, 1),
        (1, None),
    ],
)
def test_should_raise_type_error_when_ages_are_not_numbers(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
