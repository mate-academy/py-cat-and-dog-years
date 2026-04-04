from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age,dog_age,expected", [
    (0, 0, [0, 0]),
    (1, 1, [0, 0]),
    (2, 2, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (0, 5, [0, 0]),  # приклад асиметричного
    (5, 0, [0, 0]),
])
def test_get_human_age(cat_age, dog_age, expected):
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result == expected

