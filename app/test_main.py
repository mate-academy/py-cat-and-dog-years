import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="test cat and dog age zero"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="test cat and dog age below first year"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="test cat and dog age equal to first year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="test cat and dog year equal to 23"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="test cat and dog second year"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="test cat and dog third year"
        ),
        pytest.param(
            -4,
            -4,
            [0, 0],
            id="test cat and dog negative years"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="test cat and dog large number of years"
        )
    ]
)
def test_should_return_correct_values(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("12", 45),
        (45, ["12"]),
        (45, (12,)),
        ({"age": 12}, 12),
    ]
)
def test_correct_exception_if_incorrect_type(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError) as err:
        get_human_age(cat_age, dog_age)

    assert err.type == TypeError, "function must raise TypeError if incorrect type"
