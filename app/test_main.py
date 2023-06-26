import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expect_result",
    [
        (-15, -15, [0, 0]),
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (150, 150, [33, 27])
    ]
)
def test_ages(cat_age: int, dog_age: int, expect_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expect_result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param("15", 15, TypeError, id="should be raise TypeError"),
        pytest.param(14, "14", TypeError, id="should be raise TypeError")
    ]
)
def test_check_valid_input_data(cat_age: int,
                                dog_age: int,
                                expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
