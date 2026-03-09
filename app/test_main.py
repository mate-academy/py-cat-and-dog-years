from app.main import get_human_age

import pytest

def test_negative_age() -> None:
    with pytest.raises(ValueError):
        get_human_age(-5, 3)
    with pytest.raises(ValueError):
        get_human_age(5, -3)

def test_wrong_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("5", 3)
    with pytest.raises(TypeError):
        get_human_age(5, "3")


@pytest.mark.parametrize("cat_age, expected", [
    (0, 0),
    (14, 0),
    (15, 1),
    (23, 1),
    (24, 2),
    (28, 3),
    (29, 3),
    (100, 21)
])
def test_cat_age(cat_age: int, expected: int) -> None:
    assert get_human_age(cat_age, 0)[0] == expected

@pytest.mark.parametrize("dog_age, expected", [
    (0, 0),
    (14, 0),
    (15, 1),
    (23, 1),
    (24, 2),
    (28, 2),
    (29, 3),
    (100, 17)
])
def test_dog_age(dog_age: int, expected: int) -> None:
    assert get_human_age(0, dog_age)[1] == expected
