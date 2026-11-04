import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        # zero and before the first border (15)
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        # first border: 14 -> 15
        (15, 15, [1, 1]),
        # second border: 23 -> 24
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        # cat step is 4: 27 -> 28 (dog still 2)
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        # dog step is 5: 28 -> 29 (cat is already 3)
        (29, 29, [3, 3]),
        # next cat border: 31 -> 32
        (31, 31, [3, 3]),
        (32, 32, [4, 3]),
        # next dog border: 33 -> 34
        (33, 33, [4, 3]),
        (34, 34, [4, 4]),
        # different ages for cat and dog
        (28, 29, [3, 3]),
        (29, 28, [3, 2]),
        # big numbers
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected
