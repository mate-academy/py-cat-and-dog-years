import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0, 0, [0, 0],
        ),

        pytest.param(
            14, 15, [0, 1],
        ),
        pytest.param(
            23, 24, [1, 2],
        ),
        pytest.param(
            27, 27, [2, 2],
        ),
        pytest.param(
            28, 28, [3, 2]
        ),
        pytest.param(
            100, 100, [21, 17]
        ),
        pytest.param(
            -12, -12, [0, 0]
        )
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
