from __future__ import annotations
import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (1000, 1000, [246, 197]),
        (-1, -1, [0, 0])
    ],
    ids=[
        "animal ages are zeroes",
        "animal ages less than 1 human year",
        "animal ages equal 1 human year",
        "animal ages less than 2 human year",
        "animal ages equal 2 human year",
        "animal ages equal 1000 years",
        "animal ages are negative"
    ]
)
def test_get_correct_human_age(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_raise_error_when_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("10", [15])
