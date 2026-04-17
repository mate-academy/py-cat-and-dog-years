import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected_human_years",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age_conversion(
        cat_years: int,
        dog_years: int,
        expected_human_years: list[int]
) -> None:
    result = get_human_age(cat_years, dog_years)
    assert result == expected_human_years, \
        f"Expected {expected_human_years}, got {result}"


@pytest.mark.parametrize(
    "cat_years, dog_years",
    [
        (None, 12),
        (12, None),
        ("ten", 10),
        (10, "ten"),
        (21.03, 21),
        (21, 21.03)
    ]
)
def test_get_invalid_type(cat_years: int, dog_years: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)


@pytest.mark.parametrize(
    "cat_years, dog_years",
    [
        (-10, 21),
        (21, -10),
        (-1, -1)
    ]
)
def test_get_invalid_value(cat_years: int, dog_years: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_years, dog_years)
