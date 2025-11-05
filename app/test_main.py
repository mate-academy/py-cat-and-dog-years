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
        (29, 29, [3, 3]),
        (35, 40, [4, 5]),
        (50, 55, [8, 8]),
        (60, 70, [11, 11]),
        (90, 95, [18, 16]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_monotonic_increase_of_human_years() -> None:
    previous_cat, previous_dog = 0, 0
    for age in range(0, 101):
        cat, dog = get_human_age(age, age)
        assert cat >= previous_cat
        assert dog >= previous_dog
        previous_cat, previous_dog = cat, dog
