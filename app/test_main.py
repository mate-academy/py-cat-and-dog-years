from app.main import get_human_age
from typing import Any
import pytest


@pytest.mark.parametrize(
    "cat_years,dog_years,cat_years_in_human,dog_years_in_human",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (20.2, 20.1, 1, 1),
        (24, 24, 2, 2),
        (28, 28, 3, 2),
        (100, 100, 21, 17)
    ]
)
def test_get_human_age(
        cat_years: int | float,
        dog_years: int | float,
        cat_years_in_human: int,
        dog_years_in_human: int
) -> None:
    result = get_human_age(cat_years, dog_years)
    assert result == [cat_years_in_human, dog_years_in_human]


@pytest.mark.parametrize(
    "cat_years,dog_years,raised_error",
    [
        (1000, 17, ValueError),
        (-15, 25, ValueError),
        ("15", 15, TypeError)
    ]
)
def test_correct_error(
        cat_years: Any,
        dog_years: Any,
        raised_error: type[Exception]
) -> None:
    with pytest.raises(raised_error):
        get_human_age(cat_age=cat_years, dog_age=dog_years)
