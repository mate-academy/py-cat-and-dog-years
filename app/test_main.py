from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_years,dog_years,cat_years_in_human,dog_years_in_human",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (20.2, 20.1, 1, 1),
        (24, 24, 2, 2),
        (-15, 24, 0, 2),
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


def test_correct_error() -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age="15", dog_age=15)
