from app.main import get_human_age
import pytest

@pytest.mark.parametrize("cat_age, dog_age, expected",[
    (0, 0, [0, 0]),                # both below first year
    (14, 14, [0, 0]),              # both just below first year cutoff
    (15, 15, [1, 1]),              # exact first year threshold
    (23, 23, [1, 1]),              # just below second year threshold
    (24, 24, [2, 2]),              # exact second year threshold
    (27, 27, [2, 2]),              # mid-range
    (28, 28, [3, 2]),              # cat breaks into extra year group
    (100, 100, [21, 17])           # large input values
])
def test_get_human_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
