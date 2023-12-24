import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "age, expected",
    [
        pytest.param(
            13,
            [0, 0],
            id="animal age less than 1 year"
        ),
        pytest.param(
            15,
            [1, 1],
            id="animal age - 1 year"
        ),
        pytest.param(
            24,
            [2, 2],
            id="animal age - 2 years"
        ),
        pytest.param(
            28,
            [3, 2],
            id="different animal age"
        ),
        pytest.param(
            72,
            [14, 11],
            id="test random age"
        )
    ],
)
def test_get_human_age(age, expected):
    assert get_human_age(age, age) == expected
