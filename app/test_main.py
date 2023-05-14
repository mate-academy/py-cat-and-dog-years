import pytest

from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(-1, -2, [0, 0],
                     id="negative cat/dog years should convert into "
                        "0 human age"),
        pytest.param(0, 0, [0, 0],
                     id="0 cat/dog years should convert into "
                        "0 human age"),
        pytest.param(14, 14, [0, 0],
                     id="14 cat/dog years should convert into "
                        "0 human age"),
        pytest.param(15, 15, [1, 1],
                     id="15 cat/dog years should convert into "
                        "1 human age"),
        pytest.param(23, 23, [1, 1],
                     id="23 cat/dog years should convert into "
                        "1 human age"),
        pytest.param(24, 24, [2, 2],
                     id="24 cat/dog years should convert into "
                        "2 human age"),
        pytest.param(27, 28, [2, 2],
                     id="28/29 cat/dog years should convert into "
                        "2 human age"),
        pytest.param(28, 29, [3, 3],
                     id="28/29 cat/dog years should convert into "
                        "3 human age"),
        pytest.param(100, 100, [21, 17],
                     id="100 cat/dog years should convert into "
                        "21/17 human age"),
    ]
)
def test_correct_human_years(cat_age: int,
                             dog_age: int,
                             expected: list
                             ) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param({12}, "2"),
        pytest.param(2, [2])
    ]
)
def test_incorrect_type_of_data(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
