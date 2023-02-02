import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, result",
    [
        (-1, -1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (2000, 2000, [496, 397]),
    ]
)
def test_cryptocurrency_action_result(
        cat_years: int,
        dog_years: int,
        result: list
) -> None:
    assert get_human_age(cat_years, dog_years) == result
