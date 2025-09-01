import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        # zero ages
        (0, 0, [0, 0]),
        # below first threshold (<15)
        (14, 14, [0, 0]),
        # exactly at first threshold (15)
        (15, 15, [1, 1]),
        # below second threshold (15 + 9 = 24)
        (23, 23, [1, 1]),
        # exactly at second threshold (24)
        (24, 24, [2, 2]),
        # between second and third thresholds
        (27, 27, [2, 2]),
        # exactly at third threshold for cats (15+9+4=28)
        # and below third threshold for dogs (15+9+5=29)
        (28, 28, [3, 2]),
        # large ages
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_examples(cat_age, dog_age, expected):
    """
    Test get_human_age against the example cases from the specification.
    """
    assert get_human_age(cat_age, dog_age) == expected


def test_human_ages_are_integers_and_floor_divided():
    """
    Ensure that any fractional human-year remainder is discarded.
    For example, cat_age=26 → (26−24)//4 = 2//4 = 0 extra → total 2
                 dog_age=29 → (29−24)//5 = 5//5 = 1 extra → total 3
    """
    result = get_human_age(26, 29)
    assert isinstance(result[0], int) and isinstance(result[1], int)
    assert result == [2, 3]


def test_mixed_cat_and_dog_ages():
    """
    Test scenario where cat_age and dog_age map to different thresholds.
    For example, cat_age=40 → 2 + (40−24)//4 = 2 + 16//4 = 6
                 dog_age=40 → 2 + (40−24)//5 = 2 + 16//5 = 5
    """
    assert get_human_age(40, 40) == [6, 5]


def test_negative_and_zero_boundaries():
    """
    Though inputs are guaranteed valid, test explicit zero and small crossover.
    """
    # cat just below 15, dog at 15
    assert get_human_age(14, 15) == [0, 1]
    # cat at 24, dog just below 24
    assert get_human_age(24, 23) == [2, 1]
