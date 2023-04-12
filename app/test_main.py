import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
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
