import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (5, 10, [0, 0]),
    (15, 20, [1, 1]),
    (30, 40, [3, 5]),
    (10, 5, [0, 0]),
    (20, 21, [1, 1]),
    (30, 35, [3, 4]),
])
def test_age_conversion(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
