import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(
            0, 0, [0, 0],
            id="0 cat/dog years should return 0 human ages"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="less than 15 cat/dog years should return 0 human ages"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="15 cat/dog years should convert into 1 human ages"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="24 cat/dog years should convert into 2 human ages"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="28 cat years and 29 dog years should convert into 3 human ages"
        )
    ]
)
def test_convert_to_human(cat_age: int, dog_age: int, expected: list):
    assert get_human_age(cat_age, dog_age) == expected
