import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_output",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3])
    ],
    ids=[
        "both ages below first year",
        "both ages equal first year",
        "both ages below first plus second year",
        "both ages equal first plus second year",
        "dog age_one year more than cat",
        "dog age_two years more than cat"
    ]
)
def test_dog_and_cat_years_into_human_age(
        cat_age: int,
        dog_age: int,
        expected_output: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_output
