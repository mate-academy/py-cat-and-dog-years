from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (24, 24, [2, 2]),
    (35, 29, [4, 3]),
])
def test_ages(cat_age: int, dog_age: int, expected: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected


# write your code here
