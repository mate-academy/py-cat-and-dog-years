import pytest

from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_years,dog_years,human_years",
    [
        (14, 14,[0, 0]),
        (15, 23, [1, 1]),
        (32, 34, [4, 4]),
        (28, 28, [3, 2])
    ]
)
def test_should_calculate_years_correctly(cat_years,
                                          dog_years,
                                          human_years) -> None:
    assert get_human_age(cat_years, dog_years) == human_years

@pytest.mark.parametrize(
    "cat_years,dog_years,error",
    [
        (72, -5, ValueError),
        (0, 6, ValueError),
        (200, 250, ValueError),
        ("15","40", TypeError),
    ]
)
def test_input_validation(cat_years,
                          dog_years,
                          error) -> None:
    with pytest.raises(error):
        get_human_age(cat_years, dog_years)