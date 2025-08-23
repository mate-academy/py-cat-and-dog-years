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
        (15, 24, [1, 2]),
        (23, 29, [1, 3]),
        (30, 50, [3, 7]),
    ],
)
def test_various_ages(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-3, -5),
    ],
)
def test_negative_ages_raise_value_error(
    cat_age: int, dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("3", 5),
        (3, "5"),
        (3.5, 5),
        (None, 5),
        (3, None),
        ([3], 5),
        (3, {"age": 5}),
    ],
)
def test_invalid_types_raise_exception(
    cat_age: object, dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "age_before, age_after",
    [
        (14, 15),
        (23, 24),
        (27, 28),
        (29, 30),
    ],
)
def test_cat_monotonicity_at_thresholds(
    age_before: int, age_after: int
) -> None:
    assert get_human_age(age_before, 30)[0] <= get_human_age(age_after, 30)[0]


@pytest.mark.parametrize(
    "age_before, age_after",
    [
        (14, 15),
        (23, 24),
        (29, 30),
        (34, 35),
    ],
)
def test_dog_monotonicity_at_thresholds(
    age_before: int, age_after: int
) -> None:
    assert get_human_age(30, age_before)[1] <= get_human_age(30, age_after)[1]
