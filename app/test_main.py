import pytest
from app.main import get_human_age


# write your code her
@pytest.mark.parametrize(
    "cat_age, dog_age, case_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (-1, -1, [0, 0]),
        (100, 100, [21, 17])
    ]
)
def test_margin_cases(cat_age: int, dog_age: int, case_result: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == case_result


@pytest.mark.parametrize(
    "invalid_cat, invalid_dog",
    [
        ("str", 15),
        (None, 15),
        ([1, 2], 15)
    ]
)
def test_raise_type_error_value_err_none(invalid_cat: int,
                                         invalid_dog: int
                                         ) -> None:
    with pytest.raises((TypeError, ValueError)):
        get_human_age(invalid_cat, invalid_dog)
