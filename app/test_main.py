import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age, dog_age, expected, raises",
    [
        (0, 0, [0, 0], None),
        (-1, -1, None, ValueError),
        ("", "", None, TypeError),
        ([], {}, None, TypeError),
        (140000, 14000, None, ValueError),
        (14, 14, [0, 0], None),
        (15, 15, [1, 1], None),
        (23, 23, [1, 1], None),
        (24, 24, [2, 2], None),
        (27, 27, [2, 2], None),
        (28, 28, [3, 2], None),
        (100, 100, [21, 17], None),
    ]
)
def test_get_human_age(cat_age, dog_age, expected, raises):
    if raises:
        with pytest.raises(raises):
            get_human_age(cat_age, dog_age)
    else:
        assert get_human_age(cat_age, dog_age) == expected