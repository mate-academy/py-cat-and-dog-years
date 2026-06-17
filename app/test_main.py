from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age,dog_age,expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (32, 32, [4, 3]),
    (100, 100, [21, 17]),
    (100, 50, [21, 7]),
    (50, 100, [8, 17]),
    (28, 29, [3, 3]),
    (29, 30, [3, 3]),
    (1000, 1000, [246, 197]),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)


@pytest.mark.parametrize("cat_age,dog_age,expected", [
    (-5, 10, [0, 0]),
    (10, -5, [0, 0]),
    (-5, -10, [0, 0]),
])
def test_negative_ages(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age,dog_age", [
    ("15", 20),
    (20, "15"),
    (None, 20),
    (20, None),
    ([15], 20),
    (20, [15]),
    ({"years": 20}, 15)
])
def test_invalid_input_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age,expected_cat", [
    (24, 2), (25, 2), (26, 2), (27, 2),
    (28, 3),
    (31, 3),
    (32, 4),
])
def test_cat_threshold_changes(cat_age: int, expected_cat: int) -> None:
    print(get_human_age(cat_age, 0))
    assert get_human_age(cat_age, 0)[0] == expected_cat


@pytest.mark.parametrize("dog_age,expected_dog", [
    (24, 2), (25, 2), (28, 2),
    (29, 3),
    (33, 3),
    (34, 4),
])
def test_dog_threshold_changes(dog_age: int, expected_dog: int) -> None:
    assert get_human_age(0, dog_age)[1] == expected_dog
