import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,value",
    [
        (0, 0, [0, 0]),
        (200, 200, [46, 37]),
        (15, 17, [1, 1]),
        (5, 30, [0, 3]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_should_equal_to_correct_value(
        cat_age: int,
        dog_age: int,
        value: int
) -> None:
    assert get_human_age(cat_age, dog_age) == value


def test_non_integer_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", "15")


def test_negative_integer_input_should_return_empty_array() -> None:
        assert get_human_age(-15, -18) == [0, 0]


def test_float_input() -> None:
    assert get_human_age(5.6, 18.9) == [0, 1]