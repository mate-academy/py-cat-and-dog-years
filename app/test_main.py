import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [(0, 0, [0, 0]),
     (14, 14, [0, 0]),
     (15, 15, [1, 1]),
     (23, 23, [1, 1]),
     (24, 24, [2, 2]),
     (27, 27, [2, 2]),
     (28, 28, [3, 2]),
     (31, 29, [3, 3]),
     (32, 32, [4, 3]),
     (38, 34, [5, 4]),
     (41, 37, [6, 4]),
     (100, 100, [21, 17])]
)
def test_get_human_age(cat_age: int, dog_age: int,
                       expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age,dog_age", [
    ("a", 0),
    ([10, 4], 2),
    ({"a": 10, "b": 4}, 2),
    (10, 4.2),
    (5, (5, 10)),
    (None, None)
])
def test_that_input_value_is_valid_type(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age,dog_age", [
    (-5, 10),
    (-4, -1),
    (3, -5),
])
def test_that_input_values_is_valid_values(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
