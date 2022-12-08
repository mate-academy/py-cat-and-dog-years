import pytest
from app.main import get_human_age
from typing import Any


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(
            0, 0, [0, 0],
            id="should return zeros if age is 0"),
        pytest.param(
            14, 14, [0, 0],
            id="should return zeros if age less than 15"),
        pytest.param(
            15, 15, [1, 1],
            id="should return [1, 1] if age less than 24"),
        pytest.param(
            27, 27, [2, 2],
            id="should return [2, 2] if age less than 28"),
        pytest.param(
            28, 28, [3, 2],
            id="should return different values if age more than 27"),
        pytest.param(
            100, 100, [21, 17],
            id="should return expected result if pets are too old"),
        pytest.param(
            -5, -5, [0, 0],
            id="should return zeros if age is negative number")
    ]
)
def test_returns_correct_ages(
        cat_age: int,
        dog_age: int,
        expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            "1", 5, TypeError,
            id="should raise error if age not a number"),
        pytest.param(
            {1}, 5, TypeError,
            id="should raise error if age not a number")
    ]
)
def test_raises_error_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Any) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
