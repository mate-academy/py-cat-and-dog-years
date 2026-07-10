import pytest
from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (28, 100, [3, 17]),
        (100, 29, [21, 3]),
        (24, 100, [2, 17]),
        (100, 24, [21, 2]),
        (14, 100, [0, 17]),
        (100, 15, [21, 1]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    result = main.get_human_age(cat_age, dog_age)
    assert result == expected
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(age, int) for age in result)
