from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="return zeros for zeros"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="return zeros for if values < 15"
        ),
        pytest.param(
            15,
            23,
            [1, 1],
            id="return one if values in range 15 23"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="return two for both if age 27"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="cat should be older than dog"

        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should Work correct with big age"
        ),
        pytest.param(
            -15,
            -40,
            [0, 0],
            id="return zeros for negative values"
        )
    ]
)
def test_get_human_age(
        cat_age: int,

        dog_age: int,
        result: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age_incorrect,dog_age_incorrect,error",
    [
        pytest.param(
            [],
            [],
            TypeError,
            id="should raise TypeError for lists"
        ),
        pytest.param(
            " ",
            " ",
            TypeError,
            id="should raise TypeError for strings"
        ),
        pytest.param(
            {},
            {},
            TypeError,
            id="should raise TypeError for sets"
        ),
    ]
)
def test_raises_error_when_incorrect_data_type(
        cat_age_incorrect: Any,
        dog_age_incorrect: Any,
        error: Exception
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age_incorrect, dog_age_incorrect)
