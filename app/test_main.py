from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "-1, -1 should return [0, 0]",
        "0, 0 should return [0, 0]",
        "14, 14 should return [0, 0]",
        "23, 23 should return [1, 1]",
        "100, 100 should return [21, 17]",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_get_human_age_with_incorect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age(get_human_age("abc", []))
