import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),            # both ages are zero
        (14, 14, [0, 0]),          # before first human year
        (15, 15, [1, 1]),          # first human year
        (23, 23, [1, 1]),          # before second human year
        (24, 24, [2, 2]),          # second human year
        (27, 27, [2, 2]),          # before increment to third year
        (28, 28, [3, 2]),          # cat age increases, dog stays the same
        (100, 100, [21, 17]),      # large nums
    ],
    ids=[
        "zero_cat_and_dog_age",
        "before_first_human_year",
        "exact_first_human_year",
        "before_second_human_year",
        "exact_second_human_year",
        "before_third_human_year",
        "cat_ages_faster_than_dog",
        "large_ages",
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected: list[int, int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected
