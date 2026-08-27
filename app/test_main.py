import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_should_return_human_age(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (1, -5, ValueError),
        (-5, 15, ValueError),
        (-1, -1, ValueError),
    ]
)
def test_should_raises_exceptions_if_age_below_zero(
        cat_age: int,
        dog_age: int,
        result: ValueError
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
