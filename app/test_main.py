import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return zeroes when cat_age and dog_age are zeroes"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should return right values"
        ),
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="should return zeroes when (cat_age and dog age) < 0 "
        )
    ]
)
def test_cat_and_dogs_years_works_correctly(
        cat_age: int,
        dog_age: int,
        expected_human_age: list
) -> None:
    human_age = get_human_age(cat_age, dog_age)
    assert expected_human_age == human_age
