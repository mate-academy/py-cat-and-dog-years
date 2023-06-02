from typing import Any
import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0],
                     id="human age should be 0 first 14 animal years"),
        pytest.param(14, 14, [0, 0],
                     id="human age should be 0 first 14 animal years"),
        pytest.param(15, 15, [1, 1],
                     id="human age should be changed when animal age 15"),
        pytest.param(23, 23, [1, 1],
                     id="human age should be 1 next 9 years"),
        pytest.param(24, 24, [2, 2],
                     id="human age should be 2 when animal age 24"),
        pytest.param(27, 27, [2, 2],
                     id="human age should be equal when animals age <= 27"),
        pytest.param(28, 28, [3, 2],
                     id="human age should be different when animals age > 27"),
        pytest.param(100, 100, [21, 17],
                     id="test for big values"),
        pytest.param(-1, -1, [0, 0],
                     id="human age should be 0 when animals age < 0")
    ]
)
def test_ages(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        pytest.param([1], "1", TypeError,
                     id="should raise an error when age type is not int")
    ]
)
def test_raising_errors_correctly(
        cat_age: int,
        dog_age: int,
        error: Any
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
