import pytest

from app.main import get_human_age


def test_result_should_be_list() -> None:
    assert isinstance(get_human_age(0, 0), list)


def test_result_values_should_be_integers() -> None:
    for value in get_human_age(0, 0):
        assert isinstance(value, int)


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
def test_should_convert_correctly(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), f"Age values {cat_age}, {dog_age} must be converted to {result}."
