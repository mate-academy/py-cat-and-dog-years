import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_function_returns_list_of_two_integers() -> None:
    result = get_human_age(17, 18)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(age, int) for age in result)


def test_should_raise_type_error_for_incorrect_types() -> None:
    with pytest.raises(TypeError):
        get_human_age("a", "b")


def test_should_raise_value_error_for_negative_numbers() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, -10)
