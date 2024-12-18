import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, goals",
    [pytest.param(14, 14, [0, 0],
                  id="should return first 15 dog and cat years"),
     pytest.param(28, 29, [3, 3],
                  id="should return every 5 next dog and cat years"),
     pytest.param(27, 28, [2, 2],
                  id="should return every 5 next dog and cat years"),
     pytest.param(23, 23, [1, 1],
                  id="should return next 9 dog and cat years"),
     pytest.param(24, 24, [2, 2],
                  id="should return every 5 next dog and cat years"),
     pytest.param(15, 15, [1, 1],
                  id="should return next 9 dog and cat years")])
def test_cat_and_dog_years_in_human_years_correctly(cat_age: int,
                                                    dog_age: int,
                                                    goals: list) -> None:
    assert get_human_age(cat_age, dog_age) == goals


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [pytest.param([1], 1, TypeError,
                  id="should raise error when cat age is list"),
     pytest.param(1, [1], TypeError,
                  id="should raise error when dog age is list"),
     pytest.param("1", 1, TypeError,
                  id="should raise error when cat age is string"),
     pytest.param(1, "1", TypeError,
                  id="should raise error when dog age is string")])
def test_raising_errors_correctly(cat_age: int,
                                  dog_age: int,
                                  expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
