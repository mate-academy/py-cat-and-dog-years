import pytest
from app.main import get_human_age
from app import main
from typing import Any


@pytest.mark.parametrize("cat,dog,expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (-1, -1, [0, 0]),
    (-1, 15, [0, 1]),
])
def test_get_human_age(cat: int, dog: int, expected: list[int]) -> None:
    assert get_human_age(cat, dog) == expected


@pytest.mark.parametrize("cat,dog", [
    ("a", 5),
    (5, None),
    ([], 3),
])
def test_get_human_age_type_error(cat: Any, dog: Any) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat, dog)
