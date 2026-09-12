from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_ages",
    [
        pytest.param(
            5, 8,
            [0, 0],
            id="test should return zero for ages below 15"
        ),
        pytest.param(
            16, 23,
            [1, 1],
            id="test should return 1 for ages between 15 and 24"
        ),
        pytest.param(
            25, 27,
            [2, 2],
            id="test should return 2 if ages between 24 and 28"
        ),
        pytest.param(
            28, 28,
            [3, 2],
            id="test should return 3 and 2 if ages equal 28"
        ),
        pytest.param(
            100, 100,
            [21, 17],
            id="test should return 21 and 17 if ages equal 100"
        ),
        pytest.param(
            75, 46,
            [14, 6],
            id="test if ages different ages of cat and dog"
        )
    ]
)
def test_should_convert_ages_to_human_years(cat_age: int,
                                            dog_age: int,
                                            expected_ages: list[int]
                                            ) -> None:
    assert get_human_age(cat_age, dog_age) == expected_ages
