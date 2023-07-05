import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (2, 14, [0, 0]),
        (23, 15, [1, 1]),
        (24, 24, [2, 2]),
        (112, 52, [24, 7]),
        (14.3, 23.13, [0, 1]),
        (0, 0, [0, 0]),
        (-12, -3, [0, 0]),
    ]
)
def test_values(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        ("1", 1, TypeError),
        (0, dict(), TypeError),
        ((12,), 13, TypeError),
        (33, complex(3, 12), TypeError)
    ]
)
def test_exceptions(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
