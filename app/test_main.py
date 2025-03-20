import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "entry_values, expected_result",
    [
        pytest.param(
            (0, 0),
            [0, 0],
            id="should return zeroes when ages are zeroes"
        ),
        pytest.param(
            (23, 23),
            [1, 1],
            id="test when values are 23"
        ),
        pytest.param(
            (24, 24),
            [2, 2],
            id="test when values are 24"
        ),
        pytest.param(
            (28, 28),
            [3, 2],
            id="test when values are 28"
        ),
        pytest.param(
            (100, 100),
            [21, 17],
            id="test when values are 100"
        )
    ]
)
def test_get_human_age(entry_values, expected_result):
    assert get_human_age(*entry_values) == expected_result
