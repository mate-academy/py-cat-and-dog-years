import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (-2, -2, [0, 0])
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result
    assert isinstance(get_human_age(cat_age, dog_age), list)
    assert all(isinstance(element, int)
               for element in get_human_age(cat_age, dog_age))


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (4.5, "4"),
        (None, 6.7)
    ]
)
def test_get_human_age_type_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
