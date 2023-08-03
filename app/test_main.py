from app.main import get_human_age
import pytest
from typing import Any


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    pytest.param(
        0, 0, [0, 0],
        id="should return [0, 0] when years are zero"
    ),
    pytest.param(
        15, 15, [1, 1],
        id="should return [1, 1] when years are 15"
    ),
    pytest.param(
        24, 24, [2, 2],
        id="should return [2, 2] when years are 24"
    ),
    pytest.param(
        28, 29, [3, 3],
        id="should return [3, 3] when years are 28 and 29"
    ),
    pytest.param(
        28, 28, [3, 2],
        id="should return [3, 2] when years are 29"
    ),
    pytest.param(
        -1, -1, [0, 0],
        id="should return zeros when years are negative"
    ),
    pytest.param(
        100, 100, [21, 17],
        id="should return correct result when years are big"
    ),
    pytest.param(
        350, 400, [83, 77],
        id="should return correct result when years are big"
    ),
])
def test_get_human_age_result(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize("cat_age, dog_age, expected_exception", [
    pytest.param(
        1, "1",
        TypeError,
        id="should return error with incorrect type"
    ),
    pytest.param(
        "1", 1,
        TypeError,
        id="should return error with incorrect type"
    )
])
def test_get_human_age_raise_error(
        cat_age: int,
        dog_age: int,
        expected_exception: Any
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
