import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "age,expected",
    [
        pytest.param(
            14,
            [0, 0],
            id="zero year check"
        ),
        pytest.param(
            15,
            [1, 1],
            id="first year start check"
        ),
        pytest.param(
            23,
            [1, 1],
            id="first year end check"
        ),
        pytest.param(
            24,
            [2, 2],
            id="second year start check"
        ),
        pytest.param(
            27,
            [2, 2],
            id="second year for cat end check"
        ),
        pytest.param(
            28,
            [3, 2],
            id="count years for cat, second year for dog end check"
        ),
        pytest.param(
            100,
            [21, 17],
            id="count years"
        ),
    ]
)
def test_get_human_age(age, expected):
    human_age = get_human_age(age, age)
    assert human_age == expected
