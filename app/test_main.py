from app.main import get_human_age
import pytest
from typing import Any


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0], id="zero input, must be [0, 0]"),
        pytest.param(14, 14, [0, 0], id="14/14, must be [0, 0]"),
        pytest.param(15, 15, [1, 1], id="15/15, must be [1, 1]"),
        pytest.param(23, 23, [1, 1], id="23/23, must be [1, 1]"),
        pytest.param(24, 24, [2, 2], id="24/24, must be [2, 2]"),
        pytest.param(27, 27, [2, 2], id="27/27, must be [2, 2]"),
        pytest.param(28, 28, [3, 2], id="28/28, must be [3, 2]"),
        pytest.param(-1, -100, [0, 0], id="negative number"),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    )


@pytest.mark.parametrize(
    "cat_age, dog_age, expect_error",
    [
        pytest.param("1", 1,
                     TypeError, id="Please provide integer argument"),
        pytest.param([1], [2],
                     TypeError, id="Please provide integer argument"),
        pytest.param({1: 1}, {2: 3},
                     TypeError, id="Please provide integer argument")
    ]
)
def test_get_human_age_for_true_type_of_value(
        cat_age: Any,
        dog_age: Any,
        expect_error: Exception
) -> None:
    with pytest.raises(Exception):
        raise get_human_age(cat_age, dog_age)
