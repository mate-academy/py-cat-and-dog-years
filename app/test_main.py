import pytest

from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(-1, -2, [0, 0]),
        pytest.param(0, 0, [0, 0],),
        pytest.param(14, 14, [0, 0],),
        pytest.param(15, 15, [1, 1],),
        pytest.param(23, 23, [1, 1],),
        pytest.param(24, 24, [2, 2],),
        pytest.param(27, 28, [2, 2],),
        pytest.param(28, 29, [3, 3],),
        pytest.param(100, 100, [21, 17],),
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
