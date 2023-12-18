import pytest
from app.main import get_human_age
from typing import Any


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (-1, 10, [0, 0]),
    (10, -1, [0, 0]),
    (0, 10, [0, 0]),
    (10, 0, [0, 0]),
    (1000, 1000, [246, 197]),
    ("cat", 10, TypeError),
    (10, "dog", TypeError),
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: Any
) -> None:
    if expected_result == TypeError:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
    else:
        result = get_human_age(cat_age, dog_age)
        assert result == expected_result
