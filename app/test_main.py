import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_list",
    [
        pytest.param(
            0, 0, [0, 0],
            id="zero years"
        ),

        pytest.param(
            -1, -2, [0, 0],
            id="negative years"
        ),

        pytest.param(
            14, 45, [0, 6],
            id="normal years"
        ),

        pytest.param(
            56, 23, [10, 1],
            id="normal years 2"
        ),

        pytest.param(
            11893, 8919, [2969, 1781],
            id="big and not rounded years"
        ),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_list: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_list
