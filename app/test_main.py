import pytest

from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(-1, -1, [0, 0], id="test when animals 'age' < 0"),
        pytest.param(0, 0, [0, 0], id="test when animals 'age' == 0"),
        pytest.param(23, 23, [1, 1], id="test must return [1, 1] when age<24"),
        pytest.param(36, 36, [5, 4], id="test should return different age")
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert (get_human_age(cat_age, dog_age) == result)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param({0}, {0}, id="raise error when value dict"),
        pytest.param([0], [0], id="raise error when value list"),
        pytest.param("{0}", "56", id="raise error when value str")
    ]
)
def test_raise_error_if_value_not_int(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
