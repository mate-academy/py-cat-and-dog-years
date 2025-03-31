import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age,dog_age,expected", [
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (216, 214, [50, 40]),
], ids=[
    "cat_age=14, dog_age=14 (just below first threshold)",
    "cat_age=15, dog_age=15 (exactly at first threshold)",
    "cat_age=23, dog_age=23 (just below second threshold)",
    "cat_age=24, dog_age=24 (exactly at second threshold)",
    "cat_age=27, dog_age=27 (just below third threshold)",
    "cat_age=28, dog_age=28 (exactly at third threshold)",
    "cat_age=216, dog_age=214 (exactly at border threshold)"
])
def test_get_human_age_boundaries(cat_age: int,
                                  dog_age: int,
                                  expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age,dog_age", [
    (1000, 1000),
], ids=[
    "cat_age=1000, dog_age=1000 (extremely large values)"
])
def test_get_human_age_large_values(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age,dog_age", [
    (-1, 0),
    (0, -1),
    (-1, -1),
], ids=[
    "cat_age=-1, dog_age=0 (negative cat age)",
    "cat_age=0, dog_age=-1 (negative dog age)",
    "cat_age=-1, dog_age=-1 (both negative)"
])
def test_get_human_age_negative_values(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
