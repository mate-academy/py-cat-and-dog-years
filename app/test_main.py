import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cats_input, dogs_input, exception",
    [
        ("sdad", 23, TypeError),
        (22, "sad", TypeError),
        ("ten", "nine", TypeError)
    ]
)
def test_raising_error_correctly(
        cats_input: int,
        dogs_input: int,
        exception: ValueError | TypeError
) -> None:
    with pytest.raises(exception):
        get_human_age(cats_input, dogs_input)


@pytest.mark.parametrize(
    "cats_int, dogs_int, result",
    [
        (13, -13, [0, 0]),
        (12, -12, [0, 0]),
        (-10, 0, [0, 0]),
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
        result: list
) -> None:
    assert (
        get_human_age(cats_int, dogs_int) == result
    )
