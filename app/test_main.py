import pytest
from app.main import get_human_age


# write your code here
@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="should return 0 if animals have negative number"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return 0 if animals have less then 15 years"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return 1 if animals have more then 15 years"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return 2 if animals have more then 24 years"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should return every 4 next cat year in human year"
        ),
    ],
)
def test_cat_and_dog_years_in_human_years_correctly(
        cat_age: int, dog_age: int, result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
