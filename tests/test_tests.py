import pytest
from app.main import get_human_age

@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (24, 24, [1, 1]),
    (28, 28, [2, 2]),
    (50, 45, [10, 7]),
    (100, 100, [21, 17]),
])
def test_get_human_age_combined(cat_age, dog_age, expected):
    cat_result = get_human_age("cat", cat_age)
    dog_result = get_human_age("dog", dog_age)
    assert [cat_result, dog_result] == expected
