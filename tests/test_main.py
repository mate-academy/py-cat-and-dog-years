import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    'cat_age, dog_age, result',
    [
        [0, 0, [0, 0]],
        [14, 14, [0, 0]],
        [15, 23, [1, 1]],
        [24, 27, [2, 2]],
        [100, 100, [21, 17]]
    ]
)
def test_get_human_age(cat_age, dog_age, result):
    assert get_human_age(cat_age, dog_age) == result
