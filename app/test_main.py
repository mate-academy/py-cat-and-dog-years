import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_years",
    [
        pytest.param(0, 0, [0, 0], id="Mistake during convertation"),
        pytest.param(14, 14, [0, 0], id="Mistake during convertation"),
        pytest.param(15, 15, [1, 1], id="Mistake during convertation"),
        pytest.param(23, 23, [1, 1], id="Mistake during convertation"),
        pytest.param(24, 24, [2, 2], id="Mistake during convertation"),
        pytest.param(27, 28, [2, 2], id="Mistake during convertation"),
        pytest.param(28, 29, [3, 3], id="Mistake during convertation"),
        pytest.param(100, 100, [21, 17], id="Mistake during convertation"),
        pytest.param(-3, -10, [0, 0], id="If negative number passed: return 0")
    ]
)
def test_cat_age_and_dog_age_converted_to_human_age_correctly(
        cat_age: int,
        dog_age: int,
        human_years: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_years


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(
            "two",
            "eight",
            id="Should raise TypeError if passed age is not a number"
        ),
        pytest.param(
            [2],
            [8],
            id="Should raise TypeError if passed age is not a number"
        ),
        pytest.param(
            {100: 55},
            {},
            id="Should raise TypeError if passed age is not a number"
        )
    ]
)
def test_should_raise_error_if_argument_not_a_number(
        cat_age: Any,
        dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
        get_human_age(cat_age, dog_age)
        get_human_age(cat_age, dog_age)
