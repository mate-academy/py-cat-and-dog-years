import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat, dog, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17])
])
def test_get_human_age(cat: int, dog: int, expected: int) -> None:
    assert get_human_age(cat, dog) == expected


"""boundaries test"""


@pytest.mark.parametrize("cat, expected_human", [
    (0, 0),
    (14, 0),
    (15, 1),
    (23, 1),
    (24, 2),
    (27, 2),
    (28, 3),
    (32, 4),
    (36, 5)
])
def test_boundaries_cat(cat: int, expected_human: int) -> None:
    assert get_human_age(cat, 0)[0] == expected_human


@pytest.mark.parametrize("dog, expected_human", [
    (0, 0),
    (14, 0),
    (15, 1),
    (23, 1),
    (24, 2),
    (28, 2),
    (29, 3),
    (34, 4),
    (39, 5)
])
def test_boundaries_dog(dog: int, expected_human: int) -> None:
    assert get_human_age(0, dog)[1] == expected_human


# negative inputs test


@pytest.mark.parametrize("cat, dog", [
    (-1, 0),
    (0, -1),
    (-5, -3)
])
def test_invalid_inputs_negative(cat: int, dog: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat, dog)


# non-integer inputs test


@pytest.mark.parametrize("cat, dog", [
    (1.5, 2),
    ("3", 1),
    (None, 2),
    (3, [1]),
    ([1], {2}),
    (True, 10),
    (9, False)
])
def test_invalid_inputs_positive(cat: int, dog: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat, dog)
