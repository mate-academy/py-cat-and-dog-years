import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),

        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (23, 16, [1, 1]),

        (24, 24, [2, 2]),

        (27, 28, [2, 2]),

        (28, 28, [3, 2]),
        (29, 29, [3, 3]),

        (100, 100, [21, 17]),
    ],
)
def test_age_conversions_match_expected(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    )


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-10, -10),
    ],
)
def test_negative_input_should_return_zero_or_handle_appropriately(
        cat_age: int,
        dog_age: int
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == [0, 0]
    )


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("20", 20),
        (10, "10"),
        (None, 5),
    ],
)
def test_non_integer_input_should_raise_typeerror(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
