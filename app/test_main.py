import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(
            1000, 1000, [246, 197],
            id="function should handle large numbers"
        ),
        pytest.param(
            -1, -1, [0, 0],
            id="cat`s/dog`s age should be positive integer"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="correct first year for dog/cat"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="15 dog/cat year gives 1 human year"),
        pytest.param(
            24, 24, [2, 2],
            id="the next 9 dog/cat year gives one more human year"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="every 4 next cat`s year +1 extra human year"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="every 5 next dog`s year +1 extra human year"
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_age: int
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == human_age
    )


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        pytest.param(
            3, "4", TypeError,
            id="cat`s/dog`s age should be integer"
        ),
        pytest.param(
            3, [6], TypeError,
            id="cat`s/dog`s age should be integer"
        ),
        pytest.param(
            {3: 6}, 2, TypeError,
            id="cat`s/dog`s age should be integer"
        ),
    ]
)
def test_get_human_age_raise_errors_correctly(
        cat_age: int,
        dog_age: int,
        error: Exception
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
