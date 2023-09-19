import pytest
from app.main import get_human_age
from typing import List, Union, Type


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (2, 3, [0, 0]),
    (17, 20, [1, 1]),
    (-1, -5, [0, 0]),
    (0, 0, [0, 0]),
    (1000, 2000, [246, 397]),
    ("cat", "dog", TypeError),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17])

])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: Union[List[int], Type[TypeError]]
) -> None:
    if expected == TypeError:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
    else:
        assert get_human_age(cat_age, dog_age) == expected
