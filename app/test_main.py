import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_with_different_ages(
    cat_age: int,
    dog_age: int,
    expected: list,
) -> None:
    assert expected == get_human_age(cat_age, dog_age)


def test_should_raise_value_error_when_age_is_negative() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 10)


def test_should_raise_type_error_when_age_is_not_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("-1", "10")
