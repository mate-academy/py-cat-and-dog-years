from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return 0 when ages are 0"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return 0 when age < 15"
        ),
        pytest.param(
            15,
            23,
            [1, 1],
            id="should return 1 when 15 <= age <= 23"
        ),
        pytest.param(
            24,
            27,
            [2, 2],
            id="should return 2 when 24 <= age <= 27"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="cat age should be greater if age >= 28"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="Test with big ages"
        )
    ]
)
def test_human_ages_correctly(
        cat_age: int,
        dog_age: int,
        human_age: list
):
    assert get_human_age(cat_age, dog_age) == human_age
