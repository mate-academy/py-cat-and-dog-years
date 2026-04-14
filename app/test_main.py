from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected

@pytest.mark.parametrize(
    "invalid_input",[
        ("10", 10),
        (10, "10"),
        (None, 10),
        (10.5, 10),
    ]
)
def test_invalid_input(invalid_input) -> None:
    with pytest.raises(TypeError):
        get_human_age(*invalid_input)

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [(-1, 10),
     (10, -1),
     (-20, -20)]
)
def test_negative_age(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)

def test_bool_input():
    with pytest.raises(TypeError):
        get_human_age(True, 10)

def test_independent_values():
    assert get_human_age(24, 15) == [2, 1]
    assert get_human_age(15, 24) == [1, 2]