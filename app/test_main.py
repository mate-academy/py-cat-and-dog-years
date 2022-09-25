import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_ages",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return [0, 0] when inputs are equal to zeros"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return [0, 0] when inputs are "
               "one less than 1 human year"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return [1, 1] when inputs are exactly 1 human year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return [1, 1] when inputs are "
               "one less than 2 human years"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return [2, 2] when inputs are exactly 2 human years"
        ),
        pytest.param(
            27,
            28,
            [2, 2],
            id="should return [2, 2] when inputs are "
               "one less than 3 human years"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="should return [3, 3] when inputs are "
               "exactly 3 human years"
        ),
    ]
)
def test_cat_and_dog_age(cat_age: int, dog_age: int, human_ages: list[int]):
    assert get_human_age(cat_age, dog_age) == human_ages
