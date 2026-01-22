import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expect_human_age",
    [
        pytest.param(
            -1,
            -23,
            [0, 0],
            id="negative values should return 0 human years"
        ),
        pytest.param(
            0,
            14,
            [0, 0],
            id="years under 15 should return 0 human years"
        ),
        pytest.param(
            15,
            23,
            [1, 1],
            id="15 - 23 cats or dogs years should return 1 human years"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="24 - 27 cats or dogs years should return 2 human years"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="28 cats/dogs years should return 3/2 human years"
        ),
        pytest.param(
            29,
            29,
            [3, 3],
            id="29 cats or dogs years should return 3 human years"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="100 cats and dogs years should return 21 and 17 human years"
        ),
    ]
)
def test_convert_cats_and_dogs_years_to_human_years(
        cat_age: int,
        dog_age: int,
        expect_human_age: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expect_human_age


def test_invalid_data_type() -> None:
    with pytest.raises(TypeError):
        get_human_age((1, 3), "string")
