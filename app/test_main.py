import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            0, 0, [0, 0],
            id="0 cat/dog year should be 0 human years"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="14 cat/dog year should be 0 human years"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="15 cat/dog year should be 1 human years"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="23 cat/dog year should be 1 human years"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="24 cat/dog year should be 2 human years"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="27 cat/dog year should be 2 human years"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="28 cat year should be 3 human years"
        ),
        pytest.param(
            29, 29, [3, 3],
            id="29 dog year should be 3 human years"
        ),
        pytest.param(
            32, 34, [4, 4],
            id="32 cat and 34 dog year should be 4 human years"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="100 cad/dog year should be 21 and 17 human years"
        )
    ]
)
def test_correct_values(
    cat_age: int,
    dog_age: int,
    expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "10", "10", TypeError,
            id="cat/dog age should not be a string"
        ),
        pytest.param(
            ["10"], ["10"], TypeError,
            id="cat/dog age should not be a list"
        ),
        pytest.param(
            (1, 0), (1, 0), TypeError,
            id="cat/dog age should not be a tuple"
        ),
        pytest.param(
            {"cat": 1}, {"dog": 1}, TypeError,
            id="cat/dog age should not be a dict"
        ),
        pytest.param(
            {1}, {1}, TypeError,
            id="cat/dog age should not be a set"
        ),
    ]
)
def test_error_codes(
    cat_age: Any,
    dog_age: Any,
    expected_error: type
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
