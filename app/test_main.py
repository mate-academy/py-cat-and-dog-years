import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),

        (-5, -5, [0, 0]),
        (-100, -100, [0, 0]),
    ]
)
def test_get_human_age(cat_age, dog_age, expected_human_age):
    assert get_human_age(cat_age, dog_age) == expected_human_age


def test_get_human_age_invalid_input():
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")
