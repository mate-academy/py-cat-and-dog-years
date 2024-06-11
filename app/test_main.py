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
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "0 and 0 of cat and dog ages should be 0, 0 in human age",
        "14 and 14 of cat and dog ages should be 0, 0 in human age",
        "15 and 15 of cat and dog ages should be 1, 1 in human age",
        "23 and 23 of cat and dog ages should be 1, 1 in human age",
        "24 and 24 of cat and dog ages should be 2, 2 in human age",
        "27 and 27 of cat and dog ages should be 2, 2 in human age",
        "28 and 28 of cat and dog ages should be 3, 2 in human age",
        "100 and 100 of cat and dog ages should be 21, 17 in human age",
    ]
)
def test_result_in_human_age_from_cat_and_dog_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
