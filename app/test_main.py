import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, list_in_human_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="0 cat/dog years should convert into 0 human age"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="14 cat/dog years should convert into 0 human age"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="15 cat/dog years should convert into 1 human age"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="23 cat/dog years should convert into 1 human age."
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="24 cat/dog years should convert into 2 human age"
        ),
        pytest.param(
            27,
            28,
            [2, 2],
            id="27/28 cat/dog years should convert into 2 human age"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="28/29 cat/dog years should convert into 3 human age"

        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="really big age 100/100 cat/dog years should convert into 21/17"
        )
    ]
)
def test_age_should_be_converted_correctly(
        cat_age: int,
        dog_age: int,
        list_in_human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == list_in_human_age
