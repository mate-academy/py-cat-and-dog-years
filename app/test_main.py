import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            14, 14, [0, 0],
            id="should return 0 if animals are younger than 15 years"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="should return 1 if animals are between 15 and 23 years old"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="should return correct age if animals older than 24 years"
        ),
    ]
)
def test_calculates_age_correctly(
        cat_age: int,
        dog_age: int,
        result: int
) -> None:
    assert get_human_age(cat_age, dog_age) == result
