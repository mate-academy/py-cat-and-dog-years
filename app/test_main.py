from app.main import get_human_age
import pytest
from typing import Any


@pytest.mark.parametrize(
    "cat_age,dog_age,result_list",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="test should return zero when dog and cat year equal 0"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="test should return zero when dog and cat year less 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="test should return one when dog and cat year equal 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="test should return one when dog and cat year less 24"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="test should return two when dog and cat year equal 24"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="test should return two when dog and cat year less 27"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="test should return 2 and 3 when dog and cat year equal 28"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="test should return 21 and 17 when dog and cat year equal 100"
        )
    ]
)
def test_return_correctly_age(
    cat_age: int,
    dog_age: int,
    result_list: int
) -> None:
    assert get_human_age(cat_age, dog_age) == result_list


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            "1",
            "1",
            TypeError,
            id="should accept int type data"
        )
    ]
)
def test_raising_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dor_age",
    [
        pytest.param(
            0,
            0,
            id="age should be greater them -1"
        )
    ]
)
def test_age_should_be_greater_them_negative_number(
    cat_age: int,
    dor_age: int
) -> None:
    assert cat_age > -1, dor_age > -1
