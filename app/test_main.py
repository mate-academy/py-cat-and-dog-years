import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    (-1, 3, [0, 0]),                  # Test negative cat_age
    (2, -5, [0, 0]),                  # Test negative dog_age
    (-3, -2, [0, 0]),                 # Test negative cat_age and dog_age
    ("string", 30, TypeError),        # Test incorrect type for cat_age
    (10, "string", TypeError),        # Test incorrect type for dog_age
    ("string", "string", TypeError),  # Test incorrect types for both
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (28, 29, [3, 3]),
    (100, 100, [21, 17])
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list | TypeError
) -> None:
    if (
            isinstance(expected_result, type)
            and issubclass(expected_result, Exception)
    ):
        with pytest.raises(expected_result):
            get_human_age(cat_age, dog_age)
    else:
        result = get_human_age(cat_age, dog_age)
        assert result == expected_result
