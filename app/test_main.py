from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, human_years",
    [
        pytest.param(
            0, 0, [0, 0],
            id="cat/dog years = 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="first cat/dog years < 15"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="first 15 cat/dog years"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="cat/dog age > 15 but next 9 incomplete"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="9 cat/dog years = second human year"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="cat/dog years incomplete for first extra human year"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="4 cat years give 1 extra human year"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="5 dog years give 1 extra human year"
        )
    ]
)
def test_get_human_age_with_same_rules(cat_age: int,
                                       dog_age: int, human_years: int) -> None:
    assert get_human_age(cat_age, dog_age) == human_years
