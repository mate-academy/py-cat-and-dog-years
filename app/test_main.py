import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_conversion", [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age_conversion(
        cat_age: int,
        dog_age: int,
        human_conversion: int
) -> None:
    assert get_human_age(cat_age, dog_age) == human_conversion


@pytest.mark.parametrize(
    "cat_age, dog_age", [
        (-1, 5),
        (3, -50)
    ]
)
def test_negative_age_raises_error(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(ValueError, match="Age cannot be negative"):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age", [
        ("10", 5),
        (40, "8"),
        (5.8, 9),
        (7, 1.02)
    ]
)
def test_type_age_raises_error(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(TypeError, match="Age must be a natural number"):
        get_human_age(cat_age, dog_age)
