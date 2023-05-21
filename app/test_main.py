import pytest

from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0],
                     id="should return 0 when animal age is 0"
                     ),
        pytest.param(14, 14, [0, 0],
                     id="human age should be 0 first 14 animal years"),
        pytest.param(15, 15, [1, 1],
                     id="human age should be changed when animal age 15"),
        pytest.param(23, 23, [1, 1],
                     id="human age should be 1 next 9 years"),
        pytest.param(24, 24, [2, 2],
                     id="human age should be 2 when animal age 24"),
        pytest.param(27, 27, [2, 2],
                     id="converting for cat and dog"
                        " should be the same until 27"),
        pytest.param(28, 28, [3, 2],
                     id="result for cat and dog years"
                        " should be different starting from 28"),
        pytest.param(100, 100, [21, 17],
                     id="correct result for big values"),
        pytest.param(-1, -1, [0, 0],
                     id="should return 0 when animal age is negative number")

    ]
)
def test_convert_age_correctly(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:

    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param("1", "1", TypeError,
                     id="should raise error when animal age is string"),
        pytest.param([1], [1], TypeError,
                     id="should raise error when animal age is list")
    ]
)
def test_raising_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
