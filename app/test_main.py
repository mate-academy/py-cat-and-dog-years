import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(
            2, 14, [0, 0],
            id="should return 0 if pet age is less than 15"
        ),
        pytest.param(
            23, 15, [1, 1],
            id="should return 1 if pet age is >= 15 and < 24"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="should return 2 when pet is reach 24 years old"
        ),
        pytest.param(
            112, 52, [24, 7],
            id=("should raise to 1 for every extra years "
                "(4 years for cat and 5 for dog)")
        ),
        pytest.param(
            14.3, 23.13, [0, 1],
            id="should round down the float ages"
        ),
    ]
)
def test_ages(cat_age: int, dog_age: int, expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
