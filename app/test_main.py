import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_ages",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return [0, 0] when cat_age = dog_age = 0"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return [0, 0] when cat_age = dog_age = 14"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return [1, 1] when cat_age = dog_age = 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return [1, 1] when cat_age = dog_age = 23"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return [2, 2] when cat_age = dog_age = 24"
        ),
        pytest.param(
            27,
            28,
            [2, 2],
            id="should return [2, 2] when cat_age = 27 and dog_age = 28"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="should return [3, 3] when cat_age = 28 and dog_age = 29"
        ),
        pytest.param(
            105,
            105,
            [22, 18],
            id="should return [22, 18] when cat_age = dog_age = 105"
        ),
    ]
)
def test_cat_and_dog_age(cat_age: int, dog_age: int, human_ages: list[int]):
    assert get_human_age(cat_age, dog_age) == human_ages
