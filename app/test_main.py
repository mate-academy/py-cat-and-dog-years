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
    ]
)
def test_get_human_age_valid(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:

    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        (None, None, TypeError),
        ("cat", "dog", TypeError),
        ([1], [2], TypeError),  # List values
        ((1,), (2,), TypeError),  # Tuple values
        ({"age": 1}, {"age": 2}, TypeError),  # Dictionary values
    ]
)
def test_get_human_age_invalid(
        cat_age: int,
        dog_age: int,
        expected_exception: type[Exception]
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
