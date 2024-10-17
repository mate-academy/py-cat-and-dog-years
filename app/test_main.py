import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="cat and dog ages equal zero"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="cat and dog ages less then human"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="15 cat/dog years should convert into 1 human age."
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
            id="24 cat/dog years should convert into 2 human age."
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="27 cat/dog years should convert into 2 human age."
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="28 cat/dog years should convert into 3 human age."
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="100 cat/dog years should convert into 21 and 17 human age."
        ),
    ]
)
def test_get_human_age_returns_correct_values(
        cat_age: int,
        dog_age: int,
        expected: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
