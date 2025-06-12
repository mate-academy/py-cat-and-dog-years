from app.main import get_human_age
import pytest
from typing import Any


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            1,
            1,
            [0, 0],
            id="the parameters provided must be greater than -1",
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="test should return zero when dog and cat year equal 0",
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="test should return zero when dog and cat year equal 14",
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="test should return one when dog and cat year equal 15",
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="test should return one when dog and cat year equal 23",
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="test should return two when dog and cat year equal 24",
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="test should return two when dog and cat year equal 27",
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="test should return 2 and 3 when dog and cat year equal 28",
        ),
        pytest.param(
            80,
            80,
            [16, 13],
            id="test should return 16 and 13 when dog and cat age equal 80",
        ),
        pytest.param(
            150,
            150,
            [33, 27],
            id="test should return 33 and 27 when dog and cat age equal 80",
        ),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    result: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        pytest.param("1", "1", TypeError, id="string instead of int"),
        pytest.param([1], 2, TypeError, id="list instead of int"),
        pytest.param({1}, 2, TypeError, id="set instead of int"),
        pytest.param({"cat": 1}, 2, TypeError, id="dict instead of int"),
        pytest.param(None, 2, TypeError, id="None instead of int"),
    ],
)
def test_get_human_age_raises_type_error(
    cat_age: Any,
    dog_age: Any,
    expected_exception: Any,
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
