import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age, dog_age, expected_cat_human_age, expected_dog_human_age",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 27, 2, 2),
        (28, 28, 3, 3),
        (100, 100, 21, 21),
        (2, 2, 1, 1),
        (5, 5, 2, 2),
    ]
)
def test_get_human_age(cat_age, dog_age, expected_cat_human_age, expected_dog_human_age):
    cat_human_age, dog_human_age = get_human_age(cat_age, dog_age)
    assert cat_human_age == expected_cat_human_age
    assert dog_human_age == expected_dog_human_age
