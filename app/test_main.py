import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_cat_human_age", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17])
])
def test_get_human_age(cat_age: int, dog_age: int,
                       expected_cat_human_age: list
                       ) -> None:
    assert get_human_age(cat_age, dog_age) == expected_cat_human_age


@pytest.mark.parametrize("cat_age, dog_age", [
    (18, "21"),
    ("7", 11),
    ([5], 21),
    (9, {"age": 6})
])
def test_incorrect_type(
        cat_age: int,
        dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
