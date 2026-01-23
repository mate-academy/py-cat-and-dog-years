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
)
def test_should_calculate_human_age_correctly(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1),
        (-5, -5),
    ],
)
def test_should_handle_negative_ages(cat_age: int, dog_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 10),
        (10, "10"),
        (None, 5),
        (5, None),
        (10.5, 10),
        (10, 7.2),
    ],
)
def test_should_raise_type_error_for_non_integer_inputs(
    cat_age,
    dog_age,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
