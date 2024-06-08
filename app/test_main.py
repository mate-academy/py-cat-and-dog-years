import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected, not_expected",
    [
        (0, 0, [0, 0], [1, 3]),
        (14, 14, [0, 0], [2, 0]),
        (15, 15, [1, 1], [0, 0]),
        (23, 23, [1, 1], [1, 4]),
        (24, 24, [2, 2], [1, 2]),
        (27, 27, [2, 2], [3, 4]),
        (28, 28, [3, 2], [3, 4]),
        (100, 100, [21, 17], [23, 12])
    ]
)
def test_expected_ages(cat_age: int, dog_age: int, expected: list[int, int],
                       not_expected: list[int, int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected
    assert get_human_age(cat_age, dog_age) != not_expected, ("Error, please "
                                                             "check your code")
