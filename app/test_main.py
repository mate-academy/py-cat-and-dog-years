from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_cat_and_dog_ages_to_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
