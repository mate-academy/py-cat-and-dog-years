import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        pytest.param(
            0, 0, [0, 0], id="test when arguments are zero returns [0,0]"
        ),
        pytest.param(
            14, 14, [0, 0], id="test when arguments less 15 returns [0,0]"
        ),
        pytest.param(
            15, 15, [1, 1], id="test when arguments 15 returns [1,1]"
        ),
        pytest.param(
            23, 23, [1, 1], id="test when arguments 23 returns [1,1]"
        ),
        pytest.param(
            24, 24, [2, 2], id="test when arguments 24 returns [2,2]"
        ),
        pytest.param(
            28, 29, [3, 3], id="test when arguments 28/29 returns [3,3]"
        ),
        pytest.param(
            100, 100, [21, 17], id="test when arguments 100 returns [21,17]"
        ),
    ],
)
def test_get_human_age(cat_years: int, dog_years: int, expected: list) -> bool:
    assert get_human_age(cat_years, dog_years) == expected
