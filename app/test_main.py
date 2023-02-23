import pytest
from typing import List
from app.main import get_human_age


@pytest.mark.parametrize(
    "animal_age, expected_age",
    [
        (0, [0, 0]),
        (14, [0, 0]),
        (15, [1, 1]),
        (23, [1, 1]),
        (24, [2, 2]),
        (27, [2, 2]),
        (28, [3, 2]),
        (100, [21, 17]),
        (-5, [0, 0]),
        (100000, [24996, 19997]),
    ]
)
def test_get_human_age(animal_age: int, expected_age: List[int]) -> None:
    assert get_human_age(animal_age, animal_age) == expected_age


def test_get_human_age_with_invalid_input() -> None:
    with pytest.raises(TypeError, match="Animal age should be an integer"):
        get_human_age(2.5, "cat")
    with pytest.raises(TypeError, match="Animal age should be an integer"):
        get_human_age("dog", 5)
    with pytest.raises(TypeError, match="Animal age should be an integer"):
        get_human_age(5, "dog")
