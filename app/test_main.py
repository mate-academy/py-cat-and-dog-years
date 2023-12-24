import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return [0, 0] if age is 0"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return [0, 0] if age under 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return [1, 1] if age is 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return [1, 1] if age is between 15 and 24"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return [2, 2] if age is 24"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="should return [2, 2] if age is between 24 and 28"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="should return [3, 3] if the cat is 28 and the dog is 29"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should return [3, 2] for the walking dead pets"
        )
    ]
)
def test_cat_and_dog_years(
        cat_age: int, dog_age: int, expected_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age
