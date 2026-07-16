import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_should_raise_type_error_for_non_integer_ages() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 15)


def test_should_raise_value_error_for_negative_ages() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 15)
