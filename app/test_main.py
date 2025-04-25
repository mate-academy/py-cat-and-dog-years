import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_cat, expected_dog", [
    (0, 0, 0, 0),
    (14, 14, 0, 0),
    (15, 15, 1, 1),
    (23, 23, 1, 1),
    (24, 24, 2, 2),
    (27, 27, 2, 2),
    (28, 28, 3, 2),
    (100, 100, 21, 17)
])
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_cat: int,
                       expected_dog: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result[0] == expected_cat
    assert result[1] == expected_dog
