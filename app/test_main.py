import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (323, 125, [76, 22]),
        (100, 100, [21, 17]),
        (1300, 2000, [321, 397])
    ]
)
def test_big_age_values(cat_age: int, dog_age: int, result: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (f"If cat_age == {cat_age} "
        f"and dog_age == {dog_age}, the result should be {result}.")


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (14, 14, [0, 0]),
        (24, 24, [2, 2])
    ]
)
def test_small_age_value(cat_age: int, dog_age: int, result: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (f"If cat_age == {cat_age}"
        f" and dog_age == {dog_age}, the result should be {result}.")


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-1, -4, [0, 0]),
        (-100, -77, [0, 0])
    ]
)
def test_negative_numbers(cat_age: int, dog_age: int, result: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), "Age shouldn't be negative number."


def test_type_of_parameters() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", 1)
