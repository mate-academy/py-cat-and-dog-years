from typing import Type, Any
import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age_of_cat_and_dog",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (-100, -100, [0, 0]),
        (100000, 100000, [24996, 19997])
    ]
)
def test_correct_human_age(
        cat_age: int,
        dog_age: int,
        human_age_of_cat_and_dog: int
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age_of_cat_and_dog


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (1, "age", TypeError),
        (["age"], 1, TypeError),
        (1, {"dog": 1}, TypeError),
    ]
)
def test_should_raise_error_if_wrong_data_type_provided(
        cat_age: Any,
        dog_age: Any,
        result: Type[Exception]
) -> None:
    with pytest.raises(result):
        get_human_age(cat_age, dog_age)
