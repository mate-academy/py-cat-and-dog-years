import pytest

from app.main import get_human_age


def test_raising_error_correctly() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", "2")


@pytest.mark.parametrize(
    "cats_int, dogs_int, result",
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
def test_cat_and_dogs_human_years(
        cats_int: int,
        dogs_int: int,
        result: int
) -> None:
    assert (
        get_human_age(cats_int, dogs_int) == result
    )
