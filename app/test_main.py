import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="test from 0 to 14 years are 0 in humans years"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="test from 0 to 14 years are 0 in humans years"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="test from 15 to 23 years are 1 in humans years"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="test from 15 to 23 years are 1 in humans years"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="test from 24 to 27 years are 2 in humans years"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="test from 24 to 27 years are 2 in humans years"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="test cats 28 years are 3 humans years 28 dogs years are 2 humans"  # noqa: E501
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="test cats 100 years are 21 humans years 100 dogs years are 17 humans"  # noqa: E501
        ),
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="test age cannot be negative"
        ),
    ]
)
def test_basic_options(cat_age: int, dog_age: int, result: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), f"If cat's age is {cat_age} and dog's age is {dog_age}, result should be equal to {result}"  # noqa: E501
