import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (100, 100, [21, 17]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2])
    ]
)
def test_right_formula_of_calculation(cat_age: int,
                                      dog_age: int,
                                      result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_input_integer_is_negative() -> None:
    assert get_human_age(-1, -2) == [0, 0]


def test_input_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age(2, "3")
