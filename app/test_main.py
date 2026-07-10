import pytest
from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (14, 0, [0, 0]),
        (15, 0, [1, 0]),
        (0, 14, [0, 0]),
        (0, 15, [0, 1]),
        (23, 0, [1, 0]),
        (24, 0, [2, 0]),
        (0, 23, [0, 1]),
        (0, 24, [0, 2]),
        (27, 0, [2, 0]),
        (28, 0, [3, 0]),
        (0, 28, [0, 2]),
        (0, 29, [0, 3]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197]),
    ]
)
def test_get_human_age_valid(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    result = main.get_human_age(cat_age, dog_age)
    assert result == expected
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(age, int) for age in result)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (5, -1),
        (-1, -1),
    ]
)
def test_get_human_age_negative_raises(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("3", 5),
        (5, "3"),
        (3.5, 5),
        (5, 3.5),
        (None, 5),
        (5, None),
        (True, 5),
        (5, True),
    ]
)
def test_get_human_age_invalid_type_raises(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
