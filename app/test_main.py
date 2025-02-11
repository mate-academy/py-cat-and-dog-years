import pytest
from app.main import get_human_age


# write your code here
@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (32, 34, [4, 4])
    ])
def test_convert_age(cat_age, dog_age, expected) -> None:
    assert (get_human_age(cat_age, dog_age) == expected)

# def test_of_zero_years() -> None:
#     assert get_human_age(0, 0) == [0, 0]
#
#
# def test_years_more_that_15() -> None:
#     assert get_human_age(16, 16) == [1, 1]
#
#
# def test_years_more_that_24() -> None:
#     assert get_human_age(25, 25) == [2, 2]
#
#
# def test_years_more_that_30() -> None:
#     assert get_human_age(30, 31) == [3, 3]