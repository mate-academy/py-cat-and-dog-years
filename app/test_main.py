from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_various_thresholds(cat_age: int,
                                          dog_age: int,
                                          expected_result: list) -> None:
    assert (
           get_human_age(cat_age, dog_age) == expected_result)\
        , f"Should return {expected_result} for ages ({cat_age}, {dog_age})"
