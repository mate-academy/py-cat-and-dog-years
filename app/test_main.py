import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, expected_age",
    [
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
        (100, 21)
    ]
)
def test_if_the_cat_age_is_correct(cat_age: int, expected_age: int) -> None:
    assert get_human_age(cat_age, 0)[0] == expected_age


@pytest.mark.parametrize(
    "dog_age, expected_age",
    [
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (28, 2),
        (29, 3),
        (100, 17)
    ]
)
def test_if_the_dog_age_is_correct(dog_age: int, expected_age: int) -> None:
    assert get_human_age(0, dog_age)[1] == expected_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_if_the_function_works_correctly(
        cat_age: int, dog_age: int, result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-3, 5),
        (3, -2)
    ]
)
def test_if_the_function_raises_exception_if_the_age_is_negative(
        cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 3),
        (2, "2"),
        (2.5, 5),
        (1, 3.75)
    ]
)
def test_checks_if_the_function_raises_exception_in_case_of_incorrect_type(
        cat_age: str | int | float, dog_age: str | int | float
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
