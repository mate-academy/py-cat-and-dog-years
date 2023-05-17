import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "cat/dog have 0 years.",
        "cat/dog have 14 years.",
        "cat/dog have 15 years.",
        "cat/dog have 23 years.",
        "cat/dog have 24 years.",
        "cat/dog have 27/28 years.",
        "cat/dog have 28/29 years.",
        "cat/dog have 100 years."
    ]
)
def test_get_human_age_results(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
