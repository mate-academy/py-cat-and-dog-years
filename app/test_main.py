import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,human_age",
    [
        # test_14_cat_and_dog_years
        pytest.param(
            14, 14, [0, 0],
            id="For 14 cat and dog years result should be [0, 0]"
        ),
        # test_14_cat_and_dog_years
        pytest.param(
            24, 24, [2, 2],
            id="For 24 cat and dog years result should be [2, 2]"
        ),
        # test_14_cat_and_dog_years
        pytest.param(
            23, 23, [1, 1],
            id="For 23 cat and dog years result should be [1, 1]"
        ),
        # test_14_cat_and_dog_years
        pytest.param(
            15, 15, [1, 1],
            id="For 15 cat and dog years result should be [1, 1]"
        ),
        # test_14_cat_and_dog_years
        pytest.param(
            27, 28, [2, 2],
            id="For 27 cat and 28 dog years result should be [2, 2]"
        ),
        # test_14_cat_and_dog_years
        pytest.param(
            28, 29, [3, 3],
            id="For 28 cat and 29 dog years result should be [3, 3]"
        ),
    ]
)
def test_get_human_age(
        cat_years: int,
        dog_years: int,
        human_age: list
) -> None:
    assert get_human_age(cat_years, dog_years) == human_age
