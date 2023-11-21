import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    # Test cases for positive values
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (-1, -1, [0, 0]),
    (15, 24, [1, 2]),
])
def test_get_human_age_positive(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_invalid() -> None:
    # Use pytest.raises to check that the function raises the correct exception
    with pytest.raises(TypeError):
        # Pass a string as an argument
        get_human_age("cat", "dog")