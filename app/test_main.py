import pytest
from typing import Any, Type
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_ages",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "0  must be equal to [0, 0] human age",
        "14  must be equal to [0, 0] human age",
        "15  must be equal to [1, 1] human age",
        "23  must be equal to [1, 1] human age",
        "24  must be equal to [2, 2] human age",
        "27  must be equal to [2, 2] human age",
        "28  must be equal to [3, 2] human age",
        "100  must be equal to [21, 17] human age",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_ages: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_ages


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        (None, None, TypeError),
        ("10", "10", TypeError),
        ({1, 2}, {1, 2}, TypeError),
    ],
    ids=[
        "None should raise TypeError",
        "str should raise TypeError",
        "set should raise TypeError",
    ]
)
def test_test_get_human_age_errors(
        cat_age: Any,
        dog_age: Any,
        expected_error: Type[BaseException]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
