import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age_result,",
    [
        pytest.param(0, 0, [0, 0],
                     id="Check when cat's and dog's age are zero"),
        pytest.param(14, 14, [0, 0],
                     id="Check correct first year for dogs and cats"),
        pytest.param(15, 15, [1, 1],
                     id="Check last animal year before add human year"),
        pytest.param(23, 23, [1, 1],
                     id="Check correct last animal's year"),
        pytest.param(24, 24, [2, 2],
                     id="Check correct result 2 year"),
        pytest.param(28, 28, [3, 2],
                     id="Check when ages are the same, "
                        "result must be different"),
        pytest.param(100, 100, [21, 17],
                     id="Check when cat's and dog's age are big value"),
        pytest.param(-15, -15, [0, 0],
                     id="Check when cat's and dog's age are negative")
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_age_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age_result
