import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0])
    ]
)
def test_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert (get_human_age(cat_age, dog_age)) == result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("1", 0),
        (0, "1"),
        ([1], 0),
        (0, [1]),
        ({0}, 1),
        (0, {1})
    ]
)
def test_human_age_invalid_values(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
