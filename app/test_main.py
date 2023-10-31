from app.main import get_human_age
import pytest
from typing import Any


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            14, 14, [0, 0],
            id="test zero years human age limit"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="test one year human age limit"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="test two years human age limit"
        ),
        pytest.param(
            40, 50, [6, 7],
            id="test with big ages"
        ),
        pytest.param(
            -2, -2, [0, 0],
            id="test with negative ages"
        ),

        pytest.param(
            0, 0, [0, 0],
            id="test with ages as zero"
        )
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            "", "", TypeError,
            id="test with strings as ages"
        ),
        pytest.param(
            [], [], TypeError,
            id="test with list as ages"
        ),
        pytest.param(
            {}, {}, TypeError,
            id="test with dict as ages"
        ),
    ]
)
def test_incorrect_type_ages(cat_age: Any,
                             dog_age: Any,
                             expected_result: Exception) -> None:
    with pytest.raises(expected_result):
        get_human_age(cat_age, dog_age)
