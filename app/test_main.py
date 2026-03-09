import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            14, 14, [0, 0],
            id="returns zero if age is less than 15"
        ),
        pytest.param(
            15, 23, [1, 1],
            id="returns 1 if age is between 15 and 23"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="returns 2 if age more 23"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="returns 3 and more"
        ),
        pytest.param(
            37, 35, [5, 4],
            id="returns 3 and more"
        ),
        pytest.param(
            56, 40, [10, 5],
            id="returns 3 and more"
        )
    ]
)
def test_modify_cats_and_dogs_ages(cat_age, dog_age, expected) -> None:
    assert get_human_age(cat_age, dog_age) == expected
