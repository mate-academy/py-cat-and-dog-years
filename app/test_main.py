from app.main import get_human_age
import pytest
from typing import Any


@pytest.mark.parametrize(
    "cat_years, dog_years, result",
    [
        pytest.param(0, 0, [0, 0],
                     id="when arguments are zero"),
        pytest.param(14, 14, [0, 0],
                     id="when cat/dog years are less than 15"),
        pytest.param(23, 23, [1, 1],
                     id="when cat/dog years are less than 24"),
        pytest.param(27, 27, [2, 2],
                     id="when cat/dog years are less than 28"),
        pytest.param(28, 28, [3, 2],
                     id="when cat/dog years are 28"),
        pytest.param(29, 29, [3, 3],
                     id="when cat/dog years are 29"),
        pytest.param(100, 100, [21, 17],
                     id="when cat/dog years are 100"),
        pytest.param(-14, -14, [0, 0],
                     id="when cat/dog years are negative numbers"),
        pytest.param(350, 350, [83, 67],
                     id="when cat/dog years are real large numbers")

    ])
def test_should_return_correct_result(cat_years: int,
                                      dog_years: int,
                                      result: list[int]) -> None:
    assert get_human_age(cat_years, dog_years) == result


@pytest.mark.parametrize(
    "cat_years, dog_years, expected_error",
    [pytest.param([15], None, TypeError,
                  id="when input incorrect data(list and None)"),
     pytest.param("15", {}, TypeError,
                  id="when input incorrect data(str, dict)")])
def test_should_raise__error(cat_years: Any,
                             dog_years: Any,
                             expected_error: Exception) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)
