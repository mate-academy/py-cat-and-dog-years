import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (20, -1, [1, 0]),
        (-20, -1, [0, 0]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_calculate_years_correctly(
        cat_years: int,
        dog_years: int,
        result: list
) -> None:
    assert get_human_age(cat_years, dog_years) == result


@pytest.mark.parametrize(
    "cat_years,dog_years",
    [
        ("-1", 20),
        ([1, 2, 3, 4], 15),
        (1, (1, 2, 3, 4))
    ])
def test_raises_error_if_age_negative(
        cat_years: int,
        dog_years: int,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)
