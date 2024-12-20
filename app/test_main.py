import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),          # Both ages are 0
        (14, 14, [0, 0]),        # Below the first year threshold
        (15, 15, [1, 1]),        # Exactly the first year threshold
        (23, 23, [1, 1]),        # Below the second year threshold
        (24, 24, [2, 2]),        # Exactly the second year threshold
        (27, 27, [2, 2]),        # Between the second and third year threshold
        (28, 28, [3, 2]),        # Cat hits third year, dog doesn't
        (100, 100, [21, 17]),    # High ages for both
        (30, 20, [3, 3]),        # Cat and dog progress differently
        (15, 0, [1, 0]),         # Cat at first year, dog is 0
        (0, 15, [0, 1]),         # Dog at first year, cat is 0
        (20, 30, [1, 3]),
    ]
)
def test_get_human_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
