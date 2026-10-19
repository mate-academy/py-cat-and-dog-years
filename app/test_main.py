import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat, dog, result", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (-1, -1, [0, 0]),
    (15, 14, [1, 0]),
    (14, 15, [0, 1]),
    (23, 24, [1, 2]),
    (24, 23, [2, 1]),
    (27, 28, [2, 2]),
    (28, 29, [3, 3]),
    (31, 32, [3, 3]),
    (32, 33, [4, 3]),
    (33, 34, [4, 4]),
])
def test_get_human_age(cat: int, dog: int, result: list) -> None:
    assert get_human_age(cat, dog) == result


@pytest.mark.parametrize("cat, dog", [
    ("text", 20),
    (20, "text"),
    (None, 30),
    (30, None),
])
def test_human_age_invalid_type(cat: None, dog: None) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat, dog)
