import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(0, 0, [0, 0], id="should return 0 years"),
        pytest.param(14, 14, [0, 0], id="should return 0 years for both"),
        pytest.param(15, 15, [1, 1], id="should return 1 years for both"),
        pytest.param(23, 23, [1, 1], id="should return 1 years for both"),
        pytest.param(24, 24, [2, 2], id="should return 2 years for both"),
        pytest.param(27, 27, [2, 2], id="should return 2 years for both"),
        pytest.param(28, 28, [3, 2], id="should return 3 years for cat and 2 years for dog"),
        pytest.param(100, 100, [21, 17], id="should return 21 years for cat and 17 years for dog")
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param("15", 15, id="Should be an integer type"),
        pytest.param([15], 15.0, id="Should be an integer type"),
        pytest.param((15, 15), 15.0, id="Should be an integer type")
    ]
)
def test_get_human_age_for_type_errors(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
