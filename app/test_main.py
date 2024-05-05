import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(-10, -10, [0, 0], id="should return 0 years if age is negative"),
        pytest.param(0, 0, [0, 0], id="should return 0 years"),
        pytest.param(14, 14, [0, 0], id="14 cat/dog years should convert into 0 human age.]"),
        pytest.param(15, 15, [1, 1], id="15 cat/dog years should convert into 1 human age."),
        pytest.param(23, 23, [1, 1], id="23 cat/dog years should convert into 1 human age."),
        pytest.param(24, 24, [2, 2], id="24 cat/dog years should convert into 2 human age."),
        pytest.param(27, 28, [2, 2], id="27/28 cat/dog years should convert into 2 human age."),
        pytest.param(28, 29, [3, 3], id="28/29 cat/dog years should convert into 3 human age.")
    ]
)
def test_should_convert_age_(cat_age: int, dog_age: int, human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param("15", 15, id="Should be an integer type"),
        pytest.param([15], 15.0, id="Should be an integer type"),
        pytest.param((15, 15), 15.0, id="Should be an integer type")
    ]
)
def test_should_raise_type_error(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
