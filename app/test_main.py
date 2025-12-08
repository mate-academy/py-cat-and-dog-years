import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="zero cases"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="14 cases"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="first human age when cases 15, 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="first human age when cases 23, 23"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="second human age when cases 24, 24"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="second human age when cases 27, 27"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="cat +1 at 28, dog stays 2"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="large example"
        )
    ]
)
def test_parameters(cat_age, dog_age, result):
    assert get_human_age(cat_age, dog_age) == result
