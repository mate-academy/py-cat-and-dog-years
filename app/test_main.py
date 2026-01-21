import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,human_ages",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id=("when age of each animal less than 15")
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id=("when age of each animal is 15")
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id=("when age of each animal less than 24")
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id=("when age of each animal is 24")
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id=("when age of cat less than 28")
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id=("when age of each animal is calculated correctly")
        )
    ]
)
def test_get_human_age(cat: int, dog: int, human_ages: int) -> None:
    assert (
        get_human_age(cat_age=cat, dog_age=dog) == human_ages
    )
