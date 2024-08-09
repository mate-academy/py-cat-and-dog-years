import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_age_list",
    [
        pytest.param(
            14, 14, [0, 0],
            id="test first phase"
        ),
        pytest.param(
            -2, -7, [0, 0],
            id="test negative age"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="test rounding age"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="test second phase"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="test third phase"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="test old age"
        ),

    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_age_list: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age_list
