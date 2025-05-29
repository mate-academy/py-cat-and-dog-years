import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_in_age, dog_in_age, cat_out_age, dog_out_age",
    [
        (0, 14, 0, 0),
        (23, 15, 1, 1),
        (27, 24, 2, 2),
        (24, 28, 2, 2),
        (28, 29, 3, 3),
        (100, 100, 21, 17)
    ],
    ids=[
        "should be [0, 0], when `pet age` < first_year",
        "should be [1, 1], when (`1st year` < `pet age` < `1st + 2nd year`)",
        "should return `2` for cat, when `pet age` < 28",
        "should return `2` for dog, when `pet age` < 29",
        "should return `3` for cat and dog",
        "should return correct age for cat and dog"
    ]
)
def test_get_human_age(cat_in_age: int, dog_in_age: int,
                       cat_out_age: int, dog_out_age: int) -> None:
    assert get_human_age(cat_in_age, dog_in_age) == [cat_out_age, dog_out_age]
