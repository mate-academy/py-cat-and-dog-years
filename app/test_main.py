import pytest

from app.main import get_human_age


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
def test_get_human_age_normal_range(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, 10, ValueError),
        (0, -10, ValueError),
        (-1, -1, ValueError),
        ("3", 1, TypeError),
        (1, "3", TypeError),
        ("3", "3", TypeError),
        (4.5, 2, TypeError),
        (4, 3.4, TypeError),
        (4.5, 3.1, TypeError),
        (1, None, TypeError),
        (None, 10, TypeError),
        (None, None, TypeError),
    ]
)
def test_invalid_inputs(
        cat_age: int | str | None,
        dog_age: int | str | None,
        expected: Exception
) -> None:
    with pytest.raises(expected):
        get_human_age(cat_age, dog_age)
