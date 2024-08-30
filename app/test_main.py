import pytest

from app.main import get_human_age


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


@pytest.mark.parametrize(
    "cats_input, dogs_input, exception",
    [
        (-1, -1, ValueError),
        (14, -10, ValueError),
        (-15, 15, ValueError),
        ("sdad", 23, TypeError),
        (22, "sad", TypeError),
        ("ten", "nine", TypeError),
        (-1, 10, ValueError),
        (10, -1, ValueError),
        (1500, 10, ValueError),
        (10, 1500, ValueError),
        ("ten", 10, TypeError),
        (10, "ten", TypeError),
        (None, 10, TypeError),
        (10, None, TypeError),
    ]
)
def test_invalid_inputs(
        cats_input: int | str,
        dogs_input: int | str,
        exception: TypeError | ValueError
) -> None:
    with pytest.raises(exception):
        get_human_age(cats_input, dogs_input)
