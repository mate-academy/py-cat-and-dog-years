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
        (100, 100, [21, 17]),
    ],
    ids=[
        "ages_0_0: below_first_threshold",
        "ages_14_14: just_before_1yr",
        "ages_15_15: exactly_1yr",
        "ages_23_23: just_before_2yrs",
        "ages_24_24: exactly_2yrs",
        "ages_27_27: mid_second_range",
        "ages_28_28: diverging_extra_cycle",
        "ages_100_100: large_values_stress_test",
    ]
)
def test_examples(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected
