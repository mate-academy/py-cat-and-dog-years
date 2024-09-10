import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2])
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        (-1, 0, ValueError),
        (0, -1, ValueError),
        (-1, -1, ValueError),
        (2.4, 5, TypeError),
        (5, 2.4, TypeError),
        ("string", 5, TypeError),
        ({2}, "string", TypeError),
        ({3: 1}, (2), TypeError)
    ]
)
def test_invalid_values(
        cat_age: int,
        dog_age: int,
        expected_exception: type[Exception]
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
