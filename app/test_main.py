import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            0, 0, [0, 0], id="cat/dog years should convert into 0 human age."
        ),
        pytest.param(
            14, 14, [0, 0], id="cat/dog years should convert into 0 human age."
        ),
        pytest.param(
            15, 15, [1, 1], id="cat/dog years should convert into 1 human age."
        ),
        pytest.param(
            23, 23, [1, 1], id="cat/dog years should convert into 1 human age."
        ),
        pytest.param(
            24, 24, [2, 2], id="cat/dog years should convert into 2 human age."
        ),
        pytest.param(
            27, 27, [2, 2], id="cat/dog years should convert into 2 human age."
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="cat/dog years should convert into 3/2 human age."
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="cat/dog years should convert into 21/17 human age."
        ),
    ]
)
def test_cat_and_dog_age_convert_to_human(
        cat_age: int,
        dog_age: int,
        result: list,
) -> None:
    assert get_human_age(cat_age, dog_age) == result
