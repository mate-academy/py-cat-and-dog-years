from __future__ import annotations
import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (1000, 1000, [246, 197]),
        (-1, -1, [0, 0])
    ],
    ids=[
        "pet ages are 0",
        "pet ages are less than 1 human year",
        "pet ages are equal to 1 human year",
        "pet ages are less than 2 human years",
        "pet ages are equal to 2 human years",
        "pet ages are less than 3 human years",
        "pet ages are equal to 3 human years",
        "pet ages are equal to 1000 years",
        "pet ages are negative"
    ]
)
def test_get_correct_human_age(
        cat_age: int,
        dog_age: int,
        human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_raise_error_when_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("20", [20])
