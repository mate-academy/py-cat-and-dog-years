from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        pytest.param((42,), (42,), TypeError, id="test tuple values"),
        pytest.param("42", "42", TypeError, id="test strings values"),
    ],
)
def test_correct_types(
    cat_age: Any, dog_age: Any, error: type[TypeError]
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(-1, -1, [0, 0], id="test negative numbers"),
        pytest.param(0, 0, [0, 0], id="test zeroes"),
        pytest.param(13, 13, [0, 0], id="test cat 13 years and dog 13 years"),
        pytest.param(14, 14, [0, 0], id="test cat 14 years and dog 14 years"),
        pytest.param(15, 15, [1, 1], id="test cat 15 years and dog 15 years"),
        pytest.param(17, 17, [1, 1], id="test cat 17 years and dog 17 years"),
        pytest.param(24, 24, [2, 2], id="test cat 24 years and dog 24 years"),
        pytest.param(28, 28, [3, 2], id="test cat 28 years and dog 28 years"),
        pytest.param(
            60, 69, [11, 11], id="test cat 60 years and dog 69 years"
        ),
    ],
)
def test_convert_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result, (
        f"That's {result} as human years"
        f"must be after converting of {cat_age}"
        f" cat age and {dog_age} dog age"
    )
