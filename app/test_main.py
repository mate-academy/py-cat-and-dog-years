from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            -5,
            -5,
            [0, 0],
            id="check negative years of cat and dog"
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="zero age check"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="checking the limit value before 1 human year"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="checking the value transition to 1 human year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="checking the limit value before 2 human year"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="checking the value transition to 2 human year"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="checking the limit value before 3 human year"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="checking the value transition to 3 human year"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="checking large numbers"
        ),
    ]
)
def test_zero_age_check(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
