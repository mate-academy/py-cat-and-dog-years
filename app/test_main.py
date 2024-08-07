import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
    ],
    ids=[
        "14 cat/dog years should be equal to 0 human years.",
        "15 cat/dog years should be equal to 1 human year.",
        "23 cat/dog years should be equal to 1 human year.",
        "24 cat/dog years should be equal to 2 human years.",
        "27/28 cat/dog years should be equal to 2 human years.",
        "28/29 cat/dog years should be equal to 3 human years."
    ]
)
def test_converting_animal_age_to_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age

# In the checklist.md it is required to test "data out of normal range,
# such as negative numbers, zero, or really large numbers"...

# @pytest.mark.parametrize(
#     "cat_age,dog_age,expected_error",
#     [
#         (0, 0, ValueError),
#         (-1, -1, ValueError),
#         (1000, 1000, ValueError),
#         ("10", [1, 2], TypeError)
#     ],
#     ids=[
#         "should rise error if cat/dog ages equal to 0.",
#         "should rise error if cat/dog ages equal to negative number.",
#         "should rise error if cat/dog ages are large numbers.",
#         "should rise error if cat/dog ages are of incorrect type."
#     ]
# )
# def test_rising_errors_correctly(
#         cat_age: int,
#         dog_age: int,
#         expected_error: Type[Exception]
# ) -> None:
#     with pytest.raises(expected_error):
#         get_human_age(cat_age, dog_age)
