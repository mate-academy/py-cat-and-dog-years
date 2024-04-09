from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "first_age, second_age, expected_result",
    [
        pytest.param(
            14, 14, [0, 0],
            id="14 cat/dog years should convert into 0 human age."),
        pytest.param(
            15, 15, [1, 1],
            id="15 cat/dog years should convert into 1 human age."),
        pytest.param(
            23, 23, [1, 1],
            id="23 cat/dog years should convert into 1 human age."),
        pytest.param(
            24, 24, [2, 2],
            id="24 cat/dog years should convert into 2 human age."),
        pytest.param(
            27, 28, [2, 2],
            id="27/28 cat/dog years should convert into 2 human age."),
        pytest.param(
            28, 29, [3, 3],
            id="28/29 cat/dog years should convert into 3 human age."),
    ]

)
def test_get_human_age_logic(
        first_age: int,
        second_age: int,
        expected_result: list
) -> None:

    assert get_human_age(first_age, second_age) == expected_result
