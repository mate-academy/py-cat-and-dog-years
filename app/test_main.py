import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,expected",
    [
        (-1, -5, [0, 0]),
        (-5, -10, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (24, 28, [2, 2]),
    ],
)
def test_get_human_age_examples(
    cat: float,
    dog: float,
    expected: list,
) -> None:
    assert get_human_age(cat, dog) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("a", 10),
        (None, 5),
        ([1], 2),
        (1.3, 2.7),
    ],
)
def test_get_human_age_invalid_types(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
