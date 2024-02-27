import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age_list",
    [
        pytest.param(
            0, 0, [0, 0],
            id="0 cat/dog years should convert into 0 human age."
        ),
        pytest.param(
            14, 14, [0, 0],
            id="14 cat/dog years should convert into 0 human age."
        ),
        pytest.param(
            15, 15, [1, 1],
            id="15 cat/dog years should convert into 1 human age."
        ),
        pytest.param(
            23, 23, [1, 1],
            id="15 cat/dog years should convert into 1 human age."
        ),
        pytest.param(
            24, 24, [2, 2],
            id="24 cat/dog years should convert into 2 human age."
        ),
        pytest.param(
            27, 27, [2, 2],
            id="27 cat/dog years should convert into 2 human age."
        ),
        pytest.param(
            28, 28, [3, 2],
            id="28 cat/dog years should convert into 3/2 human age."
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_age_list: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age_list
