import pytest
from app.main import get_human_age


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
        (-1, -1, [0, 0]),
        (None, None, pytest.raises(TypeError)),
        ("cat", "dog", pytest.raises(TypeError)),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    if isinstance(cat_age, int) and isinstance(dog_age, int):
        assert get_human_age(cat_age, dog_age) == expected
    else:
        with expected:
            get_human_age(cat_age, dog_age)
