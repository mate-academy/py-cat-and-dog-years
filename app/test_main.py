import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_years",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="0 in cat and dog age must equal 0 in human age"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="14 in cat and dog age must equal 0 in human age"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="15 in cat and dog age must equal 1 in human age"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="23 in cat and dog age must equal 1 in human age"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="24 in cat and dog age must equal 2 in human age"
        ),
        pytest.param(
            27,
            28,
            [2, 2],
            id="27 in cat age and 28 in dog age must equal 2 in human age"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="28 in cat age and 29 in dog age must equal 3 in human age"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="100 in cat and dog age must equal 21 and 17 "
               "correspondingly in human age"
        ),
        pytest.param(
            -3,
            -10,
            [0, 0],
            id="If negative number passed: return 0"
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_years: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_years


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(
            "two",
            "eight",
            id="TypeError is raised when string is passed as parameter"
        ),
        pytest.param(
            [2],
            [8],
            id="TypeError is raised when list is passed as parameter"
        ),
        pytest.param(
            {100: 55},
            {},
            id="TypeError is raised when dict is passed as parameter"
        )
    ]
)
def test_should_raise_error_if_argument_not_a_number(
        cat_age: Any,
        dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
