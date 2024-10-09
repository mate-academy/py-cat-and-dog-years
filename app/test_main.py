import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (-1, 15, [0, 1]),
    (15, -1, [1, 0]),
    (28, 100, [3, 17]),
    (10**6, 10**6, [249996, 199997]),
    (10**8, 10**8, [24999996, 19999997]),
    (10**12, 10**12, [249999999996, 199999999997]),
])
def test_cat_years(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age", [
    ("15", 15),
    (15, "15"),
    ([15], 15),
    (15, [15]),
    ((15,), 15),
    (15, (15,)),
    ({"cat": 15}, 15),
    (15, {"dog": 15}),
])
def test_invalid_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
