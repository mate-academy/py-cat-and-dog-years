from app.main import get_human_age

import pytest

@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0])
    ],
    ids=[
        "cat: 0, dog: 0",
        "cat: 14, dog: 14",
    ]
)
def test_return_0_for_age_less_than_15(cat_years, dog_years, expected):
    actual = get_human_age(cat_years, dog_years)
    assert (actual == expected), (
        "15 cat/dog years equal to 1 human year. "
        f"Received: {actual}, when expected: {expected}"
    )

# test_return_correct_value_for_age_between_15_and_23
# get_human_age(15, 15) == [1, 1]
# get_human_age(23, 23) == [1, 1]

# test_return_correct_value_for_age_between_24_and_27
# get_human_age(24, 24) == [2, 2]
# get_human_age(27, 27) == [2, 2]

# test_return_correct_value_for_age_more_than_27
# get_human_age(28, 28) == [3, 2]
# get_human_age(100, 100) == [21, 17]
