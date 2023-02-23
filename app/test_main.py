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
        (29, [3, 3]),
        (100, [21, 17]),
        (-5, [0, 0]),
        (100000, [24996, 19997]),
    ],
    ids=[
        "animal_age_0",
        "animal_age_less_than_15",
        "animal_age_equal_to_15",
        "animal_age_between_16_and_24",
        "animal_age_equal_to_24",
        "animal_age_between_25_and_28",
        "animal_age_equal_to_28",
        "animal_age_equal_to_29",
        "animal_age_greater_than_28",
        "negative_animal_age",
        "very_large_animal_age"
    ]
)
def test_get_human_age(animal_age: int, expected_age: List[int]) -> None:
    assert get_human_age(animal_age, animal_age) == expected_age


def test_get_human_age_with_invalid_input() -> None:
    with pytest.raises(TypeError, match="'<' not supported between instances"):
        get_human_age(2, "cat")
