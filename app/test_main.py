import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (30, 20, [3, 1])
    ],
    ids=[
        "both zero age",
        "both below first year",
        "both exactly first year",
        "slightly above first year",
        "both exactly second year",
        "both slightly above second year",
        "cat older than dog",
        "both much older",
        "cat and dog different ages"
    ]
)
def test_get_human_age_valid(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
