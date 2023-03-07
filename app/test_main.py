import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (6, 10, [0, 0]),
        (15, 15, [1, 1]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (168616861, 164616461, [42154211, 32923289]),
        (-150, -13, [0, 0]),
        (150.0, 46.0, [33, 6]),
    ],
    ids=[
        "function should return 0 when cat/dog age is 0",
        "function should return 0 when cat/dog age is below 15",
        "function should return 1 when cat/dog age is 15",
        "function should return different age when cat/dog age is same",
        "function should return same age when cat/dog age is different",
        "function should work with large numbers",
        "function should return 0 when cat/dog age is negative",
        "function should work with float type cat/dog age"
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 16),
        (None, 0),
        ([13], [40]),
    ],
    ids=[
        "raise 'TypeError' if at least one value is string type",
        "raise 'TypeError' if at least one value is None type",
        "raise 'TypeError' if at least one value is list type"
    ]
)
def test_get_human_age_errors(
        cat_age: int,
        dog_age: int,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
