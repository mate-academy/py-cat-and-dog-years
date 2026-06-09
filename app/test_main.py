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
        (14, 0, [0, 0]),
        (15, 0, [1, 0]),
        (0, 23, [0, 1]),
        (0, 24, [0, 2]),
        (0, 28, [0, 2]),
        (28, 0, [3, 0]),
        (9999, 9999, [2495, 1997]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        (-5, 1, ValueError),
        (1, -5, ValueError),
        (-5, -5, ValueError),
        ([100], 4, TypeError),
        (3, {4: 1}, TypeError),
        ("3", "21", TypeError),
    ]
)
def test_raises_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
