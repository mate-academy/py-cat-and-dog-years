import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age, expectation, should_raise",
    [
        ("1", "1", pytest.raises(TypeError), True),
        (-1, -1, [0, 0], False),
        (0, 0, [0, 0], False),
        (14, 14, [0, 0], False),
        (27, 27, [2, 2], False),
        (28, 28, [3, 2], False),
        (100, 100, [21, 17], False),
    ],
    ids=[
        "test_should_raise_type_error_when_value_is_incorrect",
        "test_should_return_zero_when_value_is_negative",
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
        expectation: list,
        should_raise: bool
) -> None:
    if should_raise:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
    else:
        assert get_human_age(cat_age, dog_age) == expectation
