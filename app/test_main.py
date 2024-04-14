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
        (27, 27, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17])
    ],
    ids=[
        "test zero age",
        "test below first human age",
        "test first human age",
        "test below second human age",
        "test second human age",
        "test below third human age",
        "test third human age",
        "test above third human age"
    ]
)
def test_(cat_age: int, dog_age: int, human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
