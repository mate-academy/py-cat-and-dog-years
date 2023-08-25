import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (27, 2, [2, 0]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_correct_getting_human_age(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ({3}, 3, TypeError),
        (100, [100], TypeError),
        ("1", 1, TypeError)
    ]
)
def test_type_of_value_for_human_age(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
