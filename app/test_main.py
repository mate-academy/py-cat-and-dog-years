import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (24, 24, [2, 2]),
    (28, 28, [3, 2])
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    ), f"Test failed for cat_age={cat_age}, dog_age={dog_age}"


@pytest.mark.parametrize("cat_age, dog_age", [
    (-1, 10),
    (10, -1),
    (-1, -1),
])
def test_get_human_age_negative(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError, match="Age cannot be negative"):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age, dog_age", [
    ("fifteen", 10),
    (10, "fifteen"),
    ("fifteen", "fifteen"),
    (None, 10),
    (10, None),
    (None, None),
])
def test_get_human_age_incorrect_type(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError, match="Age must be an integer"):
        get_human_age(cat_age, dog_age)
