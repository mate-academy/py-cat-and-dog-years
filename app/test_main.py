import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_expected_ages(cat_age: int, dog_age: int,
                       expected: list[int, int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, not_expected",
    [
        (0, 0, [0, 2]),
        (14, 14, [1, 1]),
        (15, 15, [0, 0]),
        (23, 23, [3, 1]),
        (24, 24, [1, 2]),
        (27, 27, [4, 4]),
        (28, 28, [2, 5]),
        (100, 100, [26, 23])
    ]
)
def test_not_expected_ages(cat_age: int, dog_age: int,
                           not_expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) != not_expected, ("Error, please "
                                                             "check your code")
