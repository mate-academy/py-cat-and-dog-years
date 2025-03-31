import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_ages",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (32, 48, [4, 6]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "0 cat and dog ages should return [0, 0]",
        "14 cat and dog ages should return [0, 0]",
        "15 cat and dog ages should return [1, 1]",
        "23 cat and dog ages should return [1, 1]",
        "24 cat and dog ages should return [1, 1]",
        "27 cat and dog ages should return [1, 1]",
        "28 cat and dog ages should return [3, 2]",
        "32 cat and 48 dog ages should return [4, 6]",
        "100 cat and dog ages should return [21, 17]",
    ]
)
def test_animals_to_human_age(
        cat_age: int,
        dog_age: int,
        human_ages: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_ages


def test_can_convert_only_numbers() -> None:
    with pytest.raises(TypeError):
        get_human_age("2", [1, 2])
