import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            0, 0, [0, 0],
            id="Animal age 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="Animal age 14"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="Animal age 15"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="Animal age 23"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="Animal age 24"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="Animal age 27"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="Animal age 28"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="Animal age 100"
        )
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
