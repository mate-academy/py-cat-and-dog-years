from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-10, -10, [0, 0]),
        (-15, 15, [0, 1]),
        (15, -15, [1, 0]),
        (1500, 1000, [371, 197])
    ]
)
def test_expected_result_cannot_be_negative_and_really_big_numbers(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ("14", 14, TypeError),
        (14, "14", TypeError),
        ([14], 14, TypeError),
        (14, [14], TypeError),
        ({14}, 14, TypeError),
        (14, {14}, TypeError),
    ]
)
def test_raising_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: tuple
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
