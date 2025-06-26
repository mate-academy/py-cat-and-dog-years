import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
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
        (-5, 0, [0, 0]),
        (0, -5, [0, 0]),
        (-5, -5, [0, 0]),
        (5000, 5000, [1246, 997]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("10", 10),
        (10, "10"),
        ("10", "10"),
        (None, 10),
        (10, None),
        (None, None),
        ([], 10),
        (10, []),
        ([], []),
    ]
)
def test_cannot_return_age_with_wrong_type(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
