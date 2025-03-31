import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (-1, -1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17])
    ], ids=[
        "Should return [0, 0], if cat age and dog age are negative",
        "Should return [0, 0], if cat age and dog age are lower then 15",
        "Should return [1, 1], if cat age and dog age equal 15",
        "Should return [1, 1], if cat age and dog age are lower then 24",
        "Should return [2, 2], if cat age and dog age are equal 24",
        "Should return [3, 2], if cat age and dog age are equal 28",
        "Should return [3, 3], if cat age and dog age are equal 29",
        "Should return [21, 17] if cat age and dog age are equal 100"
    ]
)
def test_human_age_is_correct(
        cat_age: int,
        dog_age: int,
        human_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,error_type",
    [
        ("15", "15", TypeError),
        (None, None, TypeError),
    ], ids=[
        "Should raise TypeError, if cat and dog age are strings",
        "Should raise TypeError, if cat and dog age 'None'"
    ]
)
def test_correct_errors_when_values_are_not_correct_type(
        cat_age: int,
        dog_age: int,
        error_type: TypeError
) -> None:
    with (pytest.raises(TypeError)):
        get_human_age(cat_age, dog_age)
