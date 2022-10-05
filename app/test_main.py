import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    'cat_age, dog_age, expected',
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id='should return [0, 0] if ages are 0'
        ),
        pytest.param(
            -1,
            -1,
            [0, 0],
            id='should return [0, 0] if ages are negative'
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id='should return [0, 0] if ages < 15'
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id='should return [1, 1] if ages are 15'
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id='should return [1, 1] if ages between 15 and 24'
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id='should return [2, 2] if ages are 24'
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id='should return [3,2] if ages are 28'
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id='should return [21, 17] if ages are 100'
        )
    ]

)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
