import pytest
from typing import Any, Type
from app.main import get_human_age


@pytest.mark.parametrize(
    "cate_age, dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ], ids=["start_first_age_limit_of_dog_and_cat",
            "stop_first_age_limit_of_dog_and_cat",
            "start_second_age_limit_of_dog_and_cat",
            "stop_second_age_limit_of_dog_and_cat",
            "start_third_age_limit_of_dog_and_cat",
            "should_return_same_age_of_adult_cat_and_dog",
            "should_return_different_ages_of_adult_cat_and_dog",
            "all_ages_dog_and_cat"])
def test_age(cate_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cate_age, dog_age) == expected


@pytest.mark.parametrize(
    "cate_age, dog_age, error_age",
    [
        ("", [], TypeError),
        (-1, -10, ValueError),
    ], ids=["age_typeerror", "age_valueerror"]
)
def test_error(cate_age: Any,
               dog_age: Any,
               error_age: Type[Exception]) -> None:
    with pytest.raises(error_age):
        get_human_age(cate_age, dog_age)
