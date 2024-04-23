import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,expected",
    [
        (23, 23, [1, 1]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
    ]
)
def test_of_correct_counting(cat: int, dog: int, expected: list) -> None:
    assert get_human_age(cat, dog) == expected


def test_should_return_integer_even_if_float_input() -> None:
    assert get_human_age(15.5, 15.1) == [1, 1]


def test_should_raise_error_when_data_out_of_normal_range() -> None:
    with pytest.raises(ValueError):
        get_human_age(1000, 150)


def test_should_raise_error_when_input_data_not_a_number() -> None:
    with pytest.raises(TypeError):
        get_human_age("one", 15)
