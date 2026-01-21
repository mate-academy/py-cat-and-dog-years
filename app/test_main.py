from app.main import get_human_age
import pytest


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
        (100, 100, [21, 17]),
    ]
)
def test_should_convert_animal_years_to_human(
    cat_age: int, dog_age: int, result: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == result), (
        "'get_human_age' should return right "
        "list with converted age"
    )


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-4, -1, [0, 0]),
        (-20, 3, [0, 0]),
        (7, -18, [0, 0]),
    ]
)
def test_argument_less_than_zero(
    cat_age: int, dog_age: int, result: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == result), (
        "'get_human_age' should return zero list"
    )


def test_rise_error_while_incorrect_arguments() -> None:
    with pytest.raises(TypeError):
        get_human_age("23", 38.05)
