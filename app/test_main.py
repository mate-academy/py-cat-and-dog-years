from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
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
def test_should_return_human_age_by_list(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_raise_type_error_when_age_type_is_not_int() -> None:
    with pytest.raises(TypeError):
        get_human_age(2, "5")


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 5),
        (5, -1),
        (-2, -2)
    ]
)
def test_with_negative_age(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
