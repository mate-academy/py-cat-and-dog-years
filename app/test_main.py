from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_ages,dog_ages,result",
    [
        pytest.param(
            28, 28, [3, 2],
            id="Function should return Cat "
               "years be bigger than dog years, "
               "when the 3rd year is counted!"
        ),
        pytest.param(
            -10, -20, [0, 0],
            id="Function should return zero "
               "if years less then '0'!"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="15 animals years equal "
               "to 1 humans year!"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="Second year of animal life should be '9'!"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="Function should return rounded years!"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="the result of the function should "
               "not change the value if we pass 0!"
        )
    ]
)
def test_function_get_correct_result(
        cat_ages: int,
        dog_ages: int,
        result: list
) -> None:
    assert get_human_age(cat_ages, dog_ages) == result


def test_function_get_correct_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("28", 28)
