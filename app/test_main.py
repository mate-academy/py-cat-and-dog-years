import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (16.7, False, [1, 0]),
        (-2, -10, [0, 0])
    ],
    ids=[
        "check if cat and dog have 0 years",
        "check if 14 still give 0 for both",
        "check if value 15 gives 1 human year",
        "check border value of next 9 animal years",
        "check if 24 years gives change human years",
        "check border line for cat",
        "check border line for dog",
        "check all next years transformations",
        "check float value and bool",
        "check negative values"
    ]
)
def test_if_convertion_to_human_years_correct(
    cat_age: int, dog_age: int, result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    )


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("67", "78"),
        (6, None),
        (6, [5, 6]),
        ({"cat": 7}, {"dog": 18})
    ]
)
def test_value_type(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
