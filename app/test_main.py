import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(-1, -1, [0, 0], id="should return 0 age for ngt age"),
        pytest.param(0, 0, [0, 0], id="should return 0 years for 0 age"),
        pytest.param(14, 14, [0, 0], id="should return 0 years for both"),
        pytest.param(15, 15, [1, 1], id="should return 1 years for both"),
        pytest.param(23, 23, [1, 1], id="should return 1 years for both"),
        pytest.param(24, 24, [2, 2], id="should return 2 years for both"),
        pytest.param(27, 27, [2, 2], id="should return 2 years for both"),
        pytest.param(28, 28, [3, 2], id="should return 3/2 years for cat/dog"),
        pytest.param(415, 510, [99, 99], id="should return 99 age for cat/dog")
    ]
)
def test_should_convert_age_(cat_age: int,
                             dog_age: int,
                             human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param("15", 15, id="cat/dog age should be integer type"),
        pytest.param([15], 15.0, id="cat/dog age should be integer type"),
        pytest.param((15, 15), 15.0, id="cat/dog age should be integer type")
    ]
)
def test_should_raise_type_error(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
