import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        pytest.param((42,), (42,), TypeError, id="test tuple values"),
        pytest.param("42", "42", TypeError, id="test strings values"),
    ],
)
def test_correct_types(
        cat_age: Any,
        dog_age: Any,
        error: type[TypeError]) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(-1, -1, [0, 0], id="negative"),
        pytest.param(0, 0, [0, 0], id="zeroes"),
        pytest.param(13, 13, [0, 0], id="test 0 human years: < 15"),
        pytest.param(17, 17, [1, 1], id="test 1 human years: > 15"),
        pytest.param(24, 24, [2, 2], id="test 2 human years: equal 15 + 9"),
        pytest.param(28, 28, [3, 2], id="test start difference"),
        pytest.param(60, 69, [11, 11], id="test 11 human years"),
    ],
)
def test_convert_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result, (
        f"That's {result} as human years"
        f"must be after converting of {cat_age}"
        f" cat age and {dog_age} dog age"
    )
