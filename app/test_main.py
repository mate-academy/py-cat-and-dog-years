import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,result",
    [
        (15, 15, [1, 1]),
        (0, 0, [0, 0]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test__cat_dog_years_should_convert_into__human_age_correctly(cat_years: int, dog_years: int, result):
    assert get_human_age(cat_years, dog_years) == result


@pytest.mark.parametrize(
    "cat_years,dog_years",
    [
        (15, "15"),
        ("15", 15),
        (None, -15000),
    ]
)
def test_should_raise_error_when_incorrect_parameters(cat_years, dog_years):
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)
