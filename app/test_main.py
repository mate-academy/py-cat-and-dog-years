import pytest

from app.main import get_human_age

age_values_data = [
    (0, 0, [0, 0]),
    (15, 15, [1, 1]),
    (24, 24, [2, 2]),
    (14, 16, [0, 1]),
    (16, 14, [1, 0]),
    (27, 27, [2, 2]),
    (100, 59, [21, 9]),
]

id_values = [
    "list should be equal to [0, 0] when the values less then 15",
    "list should be equal to [1, 1] when the values between 15 and 23",
    "list should be equal to [2, 2] when the values are equal to 24",
    "list should be equal to [0, 1] "
    "when the cat age is less then 15 and dog age is between 15 and 23",
    "list should be equal to [1, 0] "
    "when the cat age between 15 and 23 and dog age is less then 15",
    "list should be equal to [2, 2] "
    "when reminder less then 'each_year' parameter",
    "list should be equal to [100, 59] "
    "when the cat and dog age are bigger then `sum((first_yer, second_yer, "
    "each_yer -1))",
]


@pytest.mark.parametrize(
    "cat_age,dog_age,expected", age_values_data, ids=id_values
)
def test_get_human_age_with_different_values(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
