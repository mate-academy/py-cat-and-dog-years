import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expectation",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "test_should_return_zero_when_value_is_zero",
        "test_should_return_zero_when_value_is_less_than_15",
        "test_should_return_2_for_cat_and_dog_when_value_is_27",
        "test_should_return_3_and_2_when_value_is_28",
        "test_should_return_21_for_cat_and_17_for_dog_when_value_is_100",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expectation: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expectation
