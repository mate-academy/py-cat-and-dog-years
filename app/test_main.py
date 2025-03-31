from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-2, -3, [0, 0]),
        (0, 0, [0, 0]),
        (6, 6, [0, 0]),
        (15, 15, [1, 1]),
        (19, 20, [1, 1]),
        (23, 23, [1, 1])
    ]
)
def test_with_negative_zero_or_small_values(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (f"If cat_age == {cat_age}  and dog_age == {dog_age},"
        f"the result should be {result}.")


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (25, 26, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_with_big_values(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (f"If cat_age == {cat_age}  and dog_age == {dog_age},"
        f"the result should be {result}.")


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("", []),
        ((), {})
    ]
)
def test_should_raise_error_if_cat_and_dog_age_not_correct_data_type(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
