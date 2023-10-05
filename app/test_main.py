import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
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
        "0 cat and dog age should be 0 human age",
        "14 cat and dog age should be 0 human age",
        "15 cat and dog age should be 1 human age",
        "23 cat and dog age should be 1 human age",
        "24 cat and dog age should be 2 human age",
        "27 cat and dog age should be 2 human age",
        "28 cat and dog age should be 3 and 2 human age",
        "100 cat and dog age should be 21 and 17 human age"
    ]
)
def test_modify_ages_correctly(cat_age: int,
                               dog_age: int,
                               expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
