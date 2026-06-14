import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
    ]
)
def test_get_human_age_valid_cases(
        cat_age: int,
        dog_age: int,
        expected_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 1),
        (10, -10),
        (-15, -15),
    ]
)
def test_should_raise_error_when_negative_numbers_or_zero(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 10),
        (10, "25"),
        (None, 10),
        (10, None),
        (10.5, 20),
        (10, 20.5)
    ]
)
def test_should_raise_error_when_invalid_types(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (51, 10),
        (10, 41),
        (100, 100),
    ]
)
def test_should_raise_error_when_age_is_realy_large_numbers(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
