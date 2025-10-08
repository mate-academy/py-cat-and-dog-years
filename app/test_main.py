import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (26, 26, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197]),
    ]
)
def test_cat_dog_human_age_conversion(cat_age: int, dog_age: int,
                                      expected_result: list) -> None:
    actual_result = get_human_age(cat_age, dog_age)
    assert actual_result == expected_result
    assert isinstance(actual_result, (list, tuple))
    assert len(actual_result) == 2
    assert all(isinstance(x, int) for x in actual_result)
