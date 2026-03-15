import pytest
from app import main

# Test1


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("1", 1),
        (1, "1"),
        ([1], 1),
        (1, [1]),
        (None, 1),
        (1, None),
        (1.5, 1),
        (1, 1.5),
        ({1}, 1),
        (1, {1}),
        (True, 1),
        (1, True),
        ((1,), 1),
        (1, (1,)),
    ],
)
def test_function_parameters_are_integers(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)


# Test2


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (7, 7),
    ],
)
def test_function_returns_list(cat_age: int, dog_age: int) -> None:
    assert (
        type(main.get_human_age(cat_age, dog_age)) is list
    ), "The function should return a list"


# Test3


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_function_calculates_human_age_correctly(
    cat_age: int, dog_age: int, expected: list
) -> None:
    result = main.get_human_age(cat_age, dog_age)
    assert result == expected, (
        f"Expected {expected} but got {result} "
        f"for cat_age={cat_age} and dog_age={dog_age}"
    )


# Test4


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 1),
        (1, -1),
    ],
)
def test_function_with_negative_ages(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)


# Test5


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (1000, 1000, [246, 197]),
        (5000, 5000, [1246, 997]),
        (10000, 10000, [2496, 1997]),
        (100000, 100000, [24996, 19997]),
        (1000000, 1000000, [249996, 199997]),
    ],
)
def test_function_with_large_ages(cat_age: int, dog_age: int, expected: list) -> None:
    assert (
        main.get_human_age(cat_age, dog_age) == expected
    ), f"Expected {expected} but got {main.get_human_age(cat_age, dog_age)}"
