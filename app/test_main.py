import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            -10,
            -10,
            [0, 0],
            id="should return 0 when pet's age is negative"
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return 0 when pet's age is 0"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return 0 when pet's age is less than 1 human year"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return 1 when pet's age is equal to 1 human year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return 1 when pet's age is less than 2 human years"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return 2 when pet's age is equal to 2 human years"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="should return 2 when pet's age is less than 3 human years"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="should return 3 when pet's age is equal to 3 human years"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should return correct age if pet's age is out of normal range"
        )
    ]
)
def test_get_correct_results(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_should_raise_typeerror_if_function_receives_incorrect_data() -> None:
    with pytest.raises(TypeError):
        get_human_age("ten", [])
