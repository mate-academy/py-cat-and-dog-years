import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected_result",
    [
        (14, 14, [0, 0]),
        (15.1, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
    ],
)
def test_ages(cat_years: int, dog_years: int, expected_result: list) -> None:
    assert get_human_age(cat_years, dog_years) == expected_result


@pytest.mark.parametrize(
    "cat_years, dog_years,expected_error",
    [
        ("14", 14, TypeError),
        (15, "15", TypeError),
        (-1, 12, ValueError),
        (10, -13, ValueError),
        (12, 0, ValueError),
        (0, 15, ValueError),
        (1000, 15, ValueError),
        (2, 250, ValueError),
    ],
)
def test_errors(cat_years: int, dog_years: int,
                expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_years, dog_years)
