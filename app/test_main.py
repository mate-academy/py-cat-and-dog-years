import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_live,dog_live,expected_result",
    [
        pytest.param(
            -5, -4, [0, 0],
            id="should be zeros, if value is negative"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="should be zeros, if arguments are zeros "
        ),

        pytest.param(
            14, 14, [0, 0],
            id="should be zeros, if arguments less than 15"
        ),

        pytest.param(
            28, 28, [3, 2],
            id="should be differences between ints of years in list"
        ),
    ]
)
def test(
        cat_live: int,
        dog_live: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_live, dog_live) == expected_result
