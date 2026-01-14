import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result, exception",
    [
        (0, 0, [0, 0], None),
        (14, 14, [0, 0], None),
        (15, 15, [1, 1], None),
        (23, 23, [1, 1], None),
        (24, 24, [2, 2], None),
        (27, 27, [2, 2], None),
        (28, 28, [3, 2], None),
        (100, 100, [21, 17], None),
        (-1, -1, [0, 0], None),
        ("3", "t", None, TypeError)
    ],
    ids=[
        "cat and dog are zeros",
        "cat and dog before one year",
        "cat and dog began one year",
        "cat and dog before two years",
        "cat and dog began two years",
        "cat and dog are 2 years",
        "cat started 3 years earlier than dog",
        "cat and dog have limit ages",
        "years outside of the normal range",
        "TypeError when incorrect types input"
    ]
)
def test_human_age_calculating(cat_age: int,
                               dog_age: int,
                               result: list,
                               exception: Exception) \
        -> None:
    if exception:
        with pytest.raises(exception):
            get_human_age(cat_age, dog_age)
    else:
        assert (get_human_age(cat_age, dog_age) == result),\
            f"Human years of {cat_age, dog_age} should be {result}"
