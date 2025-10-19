import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-1, 2, [0, 0]),
        (7, -2, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_can_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("7", "8"),
        (None, None),
        ([2], [5]),
        ((5, 3), (3, 9)),
        ({1}, {6}),
        ({3: 5}, {2: 6})
    ]
)
def test_invalid_types(cat_age, dog_age) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
