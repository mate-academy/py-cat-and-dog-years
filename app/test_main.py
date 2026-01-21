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
        (-1, 12, [0, 0]),
        (10, -13, [0, 0]),
        (12, 0, [0, 0]),
        (0, 15, [0, 1]),
        (10000, 15, [2496, 1]),
        (2, 25000, [0, 4997])
    ],
)
def test_ages(cat_years: int, dog_years: int, expected_result: list) -> None:
    assert get_human_age(cat_years, dog_years) == expected_result


@pytest.mark.parametrize(
    "cat_years, dog_years,expected_error",
    [
        ("14", 14, TypeError),
        (15, "15", TypeError)
    ]
)
def test_errors(cat_years: int, dog_years: int,
                expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_years, dog_years)
