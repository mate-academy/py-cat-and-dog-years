import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    pytest.param(
        0, 0, [0, 0],
        id="zero ages should return zeros"
    ),
    pytest.param(
        14, 14, [0, 0],
        id="ages below 15 should return zeros"
    ),
    pytest.param(
        15, 15, [1, 1],
        id="15 years should return one"
    ),
    pytest.param(
        23, 23, [1, 1],
        id="16 to 23 years should return one"
    ),
    pytest.param(
        24, 24, [2, 2],
        id="24 years should return two"
    ),
    pytest.param(
        27, 27, [2, 2],
        id="25 to 27 years should return two"
    ),
    pytest.param(
        28, 28, [3, 2],
        id="cat 28 years should return three, dog should return two"
    ),
    pytest.param(
        100, 100, [21, 17],
        id="large ages"
    ),
    pytest.param(
        -1, -1, [0, 0],
        id="negative ages should return zeros"
    ),
    pytest.param(
        32, 32, [4, 3],
        id="cat 32 and dog 34 should return four "),

])
def test_ages(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
