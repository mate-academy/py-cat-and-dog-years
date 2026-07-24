import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -10, [0, 0]),
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [7, 6]),
        (11, 11, [0, 0]),
        (20, 20, [1, 1]),
        (28, 29, [8, 7]),
        (32, 34, [9, 8]),
        (6002, 7502, [1502, 1502])
    ]
)
def test_all_functionality_have_to_work_correctly(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ("10", "1", TypeError),
        ([3], {4}, TypeError),
        ((1,), {2: 3}, TypeError),
    ]
)
def test_raise_error_if_type_of_input_data_is_incorrect(
        cat_age: int,
        dog_age: int,
        expected_error: type[TypeError]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
