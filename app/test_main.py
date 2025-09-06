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
        (100, 100, [21, 17])
    ],
    ids=[
        "the age of the animals must be 0.",
        "the age of the animals must be 0.",
        "age of animals should be equal 1.",
        "age of animals should be equal 1.",
        "age of animals should be equal 2.",
        "age of animals should be equal 2.",
        "cat age should be larger than dog's.",
        "difference between ages equals 4.",
    ]
)
def test_modify_animals_age_correctly(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
