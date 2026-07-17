import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cats_age, dogs_age, result",
    [
        pytest.param(
            12, 14,
            [0, 0],
            id="Should return 0 if dogs and cats age less than 15"
        ),
        pytest.param(
            24, 24,
            [2, 2],
            id="Counting 9 cats and dogs years as 1 human year after 15"
        ),
        pytest.param(
            44, 0,
            [7, 0],
            id="Counting every 4 cats years as 1 human year after 24"
        ),
        pytest.param(
            0, 39,
            [0, 5],
            id="Counting every 5 dogs years as 1 human year after 24"
        ),
        pytest.param(
            15, 0,
            [1, 0],
            id="Should return 1 if dogs or cats age is equal 15"
        ),
        pytest.param(
            23, 26,
            [1, 2],
            id="Should return 1 if dogs or cats age is 23"
        )
    ]
)
def test_function_working_correctly(
    cats_age: int,
    dogs_age: int,
    result: list
) -> None:
    assert get_human_age(cats_age, dogs_age) == result
