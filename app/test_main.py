from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, converted_age",
    [
        (-1, -1, [0, 0]),
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
def test_human_age_converted_from_cat_and_dog(
        cat_age: int,
        dog_age: int,
        converted_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == converted_age


def test_incorrect_input_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", "0")
