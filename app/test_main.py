from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "initial_age, expect_age",
    [
        pytest.param(
            [0, 0],
            [0, 0],
            id="should equal to zero"
        ),
        pytest.param(
            [14, 14],
            [0, 0],
            id="one human year should equal below 15 year of both"
        ),
        pytest.param(
            [15, 15],
            [1, 1],
            id="one human year should equal 15 year of both"
        ),
        pytest.param(
            [23, 23],
            [1, 1],
            id="one human year should equal below 24 year of both"
        ),
        pytest.param(
            [24, 24],
            [2, 2],
            id="second human year should add 9 years of both"
        ),
        pytest.param(
            [28, 29],
            [3, 3],
            id="next human years should add 4 cat years and 5 dog years"
        )
    ]
)
def test_age_correctly(initial_age: list, expect_age: list) -> None:
    assert get_human_age(initial_age[0], initial_age[1]) == expect_age


@pytest.mark.parametrize(
    "initial_age, expect_error",
    [
        pytest.param(
            "abs",
            TypeError,
            id="should raise error when parameter is not int"
        ),
    ]
)
def test_raising_error(initial_age: list, expect_error: any) -> None:
    with pytest.raises(expect_error):
        assert get_human_age(initial_age)

