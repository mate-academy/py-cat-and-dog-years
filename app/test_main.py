import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "initial_cat_age,initial_dog_age,expected_result",
    [
        (14, 12, [0, 0]),
        (15, 23, [1, 1]),
        (24, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "animal age less than 15 should convert to 0",
        "animal age from 15 to 23 should convert to 1",
        "animal age from 24 to 27 should convert to 2",
        "cat age 28 should convert to 3",
        "animal age over 28 should be converted according to requirements",
    ]
)
def test_get_human_age(
        initial_cat_age: int,
        initial_dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(initial_cat_age, initial_dog_age) == expected_result
