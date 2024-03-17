import pytest
from app.main import get_human_age


@ pytest.mark.parametrize(
    "threshold_min_value_cat_age,"
    "threshold_min_value_dog_age,"
    "threshold_max_value_cat_age,"
    "threshold_max_value_dog_age,"
    "human_age",
    [
        pytest.param(
            14, 14, 0, 0,
            [0, 0],
            id="test should return 0 for first 14 animal years"
        ),
        pytest.param(
            15, 15, 23, 23,
            [1, 1],
            id="test should return 1 for first 15-23 animal years"
        ),
        pytest.param(
            24, 24, 27, 28,
            [2, 2],
            id="test should return 2 for first 24-27 cat and 24-28 dog years"
        )
    ]
)
def test(
        threshold_min_value_cat_age: int,
        threshold_min_value_dog_age: int,
        threshold_max_value_cat_age: int,
        threshold_max_value_dog_age: int,
        human_age: list,
) -> None:

    assert (
        get_human_age(
            threshold_min_value_cat_age,
            threshold_min_value_dog_age
        ) == get_human_age(
            threshold_max_value_cat_age,
            threshold_max_value_dog_age
        ) == human_age
    )
