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
    ],
)
def test_examples(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (0, 0),
        (10, 10),
        (15, 15),
        (24, 24),
        (28, 28),
        (50, 50),
        (100, 100),
    ],
)
def test_result_length(cat_age: int, dog_age: int) -> None:
    result = main.get_human_age(cat_age, dog_age)
    assert len(result) == 2


@pytest.mark.parametrize(
    "cat_age",
    [0, 5, 14, 15, 23, 24, 50, 100],
)
def test_cat_human_age_is_integer(cat_age: int) -> None:
    result = main.get_human_age(cat_age, 0)
    assert isinstance(result[0], int)


@pytest.mark.parametrize(
    "dog_age",
    [0, 5, 14, 15, 23, 24, 50, 100],
)
def test_dog_human_age_is_integer(dog_age: int) -> None:
    result = main.get_human_age(0, dog_age)
    assert isinstance(result[1], int)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (15, 0),
        (24, 0),
        (28, 0),
        (100, 0),
    ],
)
def test_cat_and_dog_are_calculated_independently(
    cat_age: int,
    dog_age: int,
) -> None:
    result = main.get_human_age(cat_age, dog_age)
    cat_result = main.get_human_age(cat_age, 0)[0]
    dog_result = main.get_human_age(0, dog_age)[1]
    assert result == [cat_result, dog_result]


@pytest.mark.parametrize(
    "cat_age",
    [
        15,
        24,
        28,
        100,
    ],
)
def test_cat_age_increases_monotonically(cat_age: int) -> None:
    younger = main.get_human_age(cat_age - 1, 0)[0]
    older = main.get_human_age(cat_age, 0)[0]
    assert older >= younger


@pytest.mark.parametrize(
    "dog_age",
    [
        15,
        24,
        28,
        100,
    ],
)
def test_dog_age_increases_monotonically(dog_age: int) -> None:
    younger = main.get_human_age(0, dog_age - 1)[1]
    older = main.get_human_age(0, dog_age)[1]
    assert older >= younger
