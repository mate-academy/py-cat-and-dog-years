import pytest

from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age,dog_age,expected_cat_human_age,expected_dog_human_age",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (23, 23, 1, 1),
        (27, 27, 2, 2),
        (28, 28, 3, 2),
        (29, 29, 3, 3),
    ]
)
def test_main_get_human_age(cat_age: int, dog_age: int, expected_cat_human_age: int, expected_dog_human_age: int) -> None:
    actual_cat_human_age, actual_dog_human_age = get_human_age(cat_age, dog_age)
    assert actual_cat_human_age == expected_cat_human_age and actual_dog_human_age == expected_dog_human_age
