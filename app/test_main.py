import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_years, dog_years, expected_result", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (40, 40, [6, 5]),
    (100, 100, [21, 17]),
    (-1, 15, [0, 1]),
    (15, -1, [1, 0]),
])
def test_human_age_conversion(
        cat_years: int, dog_years: int, expected_result: list
) -> None:
    assert get_human_age(cat_years, dog_years) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        (0, bool, TypeError),
        (3.5, "cat", TypeError),
        (10, 10.5, TypeError),
        (10.5, 10.5, TypeError),
        ("cat", 10, TypeError),
        (10, "dog", TypeError),
        ("cat", "dog", TypeError),
    ]
)
def test_error_type_ages(
        cat_age: int,
        dog_age: int,
        expected_error: list[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
