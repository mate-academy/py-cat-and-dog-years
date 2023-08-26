import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            14,
            0,
            [0, 0],
            id="should add zero to list if cat_age or dog_age less than first_year"
        ),
        pytest.param(
            20,
            21,
            [1, 1],
            id="should add 1 to list if we use only first_year rule"
        ),
        pytest.param(
            25,
            26,
            [2, 2],
            id=("should add 2 to list if we use"
                " first_year and second_year rule")
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id=("should return correct values if we use"
                " first_year, second_year and each_year rules")
        ),
    ]
)
def test_check_correct_result(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
