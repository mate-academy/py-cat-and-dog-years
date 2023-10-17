import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        pytest.param(
            -10, -10, [0, 0],
            id="should convert into 0 human age, "
               "if animal years is negative integer"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="should convert into 0 human age, "
               "if animal years is zero"
        ),
        pytest.param(
            10, 10, [0, 0],
            id="should return human age = 0, "
               "if animal years is less than 15"
        ),
        pytest.param(
            20, 20, [1, 1],
            id="should return human age = 1, "
               "if animal ages is less than 24"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="should return human age = 2, "
               "if ages cat is less than 28"
               "and should return human age = 2, "
               "if ages dog is less than 29"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="should return human age = 3, "
               "if ages cat is great than 27"
               "and should return human age = 3, "
               "if ages dog is great than 28"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="check long life animals"
        ),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age
