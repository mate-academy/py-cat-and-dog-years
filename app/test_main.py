import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,expected_years",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-11, -11, [0, 0])
    ]
)
def test_need_to_get_correct_human_years(
        cat_years: int,
        dog_years: int,
        expected_years: list
) -> None:
    assert get_human_age(cat_years, dog_years) == expected_years


@pytest.mark.parametrize(
    "cat_years,dog_years",
    [
        (1, "1"),
        ("1", 1),
    ]
)
def test_expected_error(cat_years: Any, dog_years: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)
