import pytest
from app.main import get_human_age

@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (29, 29, [3, 3]),  # Just after boundary for dog
    (100, 100, [21, 17]),

    # Negative age input tests – expect [0,0]
    (-1, -1, [0, 0]),
    (-5, -10, [0, 0]),

    # Mixed negative and positive inputs
    (-5, 15, [0, 1]),
    (15, -10, [1, 0]),
])
def test_get_human_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_invalid_types():
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")

    with pytest.raises(TypeError):
        get_human_age(10.5, 12.5)

    with pytest.raises(TypeError):
        get_human_age(None, [])

    with pytest.raises(TypeError):
        get_human_age({}, 5)
