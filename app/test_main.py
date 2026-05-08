import pytest
import app.main as main


VALID_DATA = [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (15, 0, [1, 0]),
    (0, 15, [0, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (24, 23, [2, 1]),
    (23, 24, [1, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (28, 29, [3, 3]),
    (100, 100, [21, 17]),
    (-1, -1, [0, 0]),
    (1000, 1000, [246, 197]),
]

INVALID_DATA = [
    ("10", 10),
    (10, "10"),
    (None, 10),
    (10, None),
    (10.5, 10),
    (10, 10.5),
    ([], 10),
    (10, {}),
]


@pytest.mark.parametrize("cat_age,dog_age,expected", VALID_DATA)
def test_valid(cat_age: int, dog_age: int, expected: list) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age,dog_age", INVALID_DATA)
def test_invalid(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
