from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (14, 12, [0, 0]),  # Testing when both animals are less than the first year
    (15, 23, [1, 1]),  # Testing when both animals are one year old
    (28, 28, [3, 2]),  # Testing when both animals are two years old
    (-1, 5, None),  # Testing negative cat_age
    (5, -1, None),  # Testing negative dog_age
    (0, 5, None),  # Testing zero cat_age
    (5, 0, None),  # Testing zero dog_age
    (1000000, 5, None),  # Testing very large cat_age
    (5, 1000000, None),  # Testing very large dog_age
    (5, 5.5, None),  # Testing dog_age as float
    ('5', 5, None),  # Testing cat_age as string
    (5, '5', None),  # Testing dog_age as string
    (5, 5, None),  # Testing each_year as 0
])
def test_get_human_age(cat_age, dog_age, expected):
    if expected is None:
        with pytest.raises((TypeError, ValueError)):
            get_human_age(cat_age, dog_age)
    else:
        assert get_human_age(cat_age, dog_age) == expected
