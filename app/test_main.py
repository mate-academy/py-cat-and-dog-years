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
        (1, 0, [0, 0]),
        (0, 1, [0, 0]),
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
        (24, 0, [2, 0]),
        (1000, 1000, [246, 197]),
        (10000, 10000, [2496, 1997]),
        (-1, 15, [0, 1]),
        (15, -1, [1, 0]),
        (-1, -1, [0, 0]),
        ("string", 10, pytest.raises(TypeError)),
        (10, "string", pytest.raises(TypeError)),
        ("string", "string", pytest.raises(TypeError)),
        (None, 10, pytest.raises(TypeError)),
        (10, None, pytest.raises(TypeError)),
        (None, None, pytest.raises(TypeError))
    ]
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: get_human_age
) -> None:
    if isinstance(expected, list):
        assert get_human_age(cat_age, dog_age) == expected
    else:
        with expected:
            get_human_age(cat_age, dog_age)
