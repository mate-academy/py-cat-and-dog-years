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
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "cat and dog are zeros",
        "cat and dog before one year",
        "cat and dog began one year",
        "cat and dog before two years",
        "cat and dog began two years",
        "cat and dog are 2 years",
        "cat started 3 years earlier than dog",
        "cat and dog have limit ages"
    ]
)
def test_human_age_calculating(cat_age: int, dog_age: int, result: list) \
        -> None:
    assert (get_human_age(cat_age, dog_age) == result),\
        f"Human years of {cat_age, dog_age} should be {result}"
