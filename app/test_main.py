import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 27, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "both_zero",
        "both_less_than_15",
        "both_15",
        "both_between_15_and_24",
        "both_24",
        "both_between_24_and_27",
        "cat_28_dog_27",
        "cat_100_dog_100",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
