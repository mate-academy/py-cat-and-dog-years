import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        [0, 0, [0, 0]],
        [15, 15, [1, 1]],
        [24, 24, [2, 2]],
        [26, 26, [2, 2]],
        [28, 28, [3, 2]],
        [29, 29, [3, 3]]
    ]
)
def test_get_human_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
