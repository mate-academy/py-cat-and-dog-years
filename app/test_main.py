from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(-1, -1, [0, 0],
                     id="Age of pets should be positive number"),
        pytest.param(0, 0, [0, 0],
                     id="Zero ages for pets are 0 for people"),
        pytest.param(14, 14, [0, 0],
                     id="First 15 pets years give 1 human year"),
        pytest.param(15, 15, [1, 1],
                     id="First 15 pets years give 1 human year"),
        pytest.param(23, 23, [1, 1],
                     id="The next 9 pets years give 1 more human year"),
        pytest.param(24, 24, [2, 2],
                     id="The next 9 pets years give 1 more human year"),
        pytest.param(27, 27, [2, 2],
                     id="The next 9 pets years give 1 more human year"),
        pytest.param(28, 28, [3, 2],
                     id="Every 4 next cat years give 1 extra human year"),
        pytest.param(100, 100, [21, 17],
                     id="Every 4 next cat years give 1 extra human year"),
    ]
)
def test_correct_math(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
