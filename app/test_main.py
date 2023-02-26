import pytest

from app.main import get_human_age

age_values_data = [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 29, [3, 3]),
    (-2, -3, [0, 0]),
    (1256987, 268852, [314242, 53767])
]

id_values = [
    "list should be equal to [0, 0] when the values are less then 15",
    "list should be equal to [0, 0] when the values "
    "are equal 'zero' yer top edge(14)",
    "list should be equal to [1, 1] when the values "
    "are equal 'first' yer bottom edge(15)",
    "list should be equal to [1, 1] when the values "
    "are equal 'first' yer top edge(23)",
    "list should be equal to [2, 2] when the values "
    "are equal 'second' yer bottom edge(24)",
    "list should be equal to [2, 2] when the values "
    "are top edge of 'second' yer: "
    "bottom edge + 'each_yer'",
    "list should be equal to [3, 3] when the values "
    "are bigger than 'second' top edge",
    "list should be equal to [0, 0] when the values are negative",
    "list should be equal to [314242, 53767] when the function"
    " is handling large numbers like '1256987', '268852'"
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


def test_raise_an_error_if_values_are_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 15)
        get_human_age(15, "15")
