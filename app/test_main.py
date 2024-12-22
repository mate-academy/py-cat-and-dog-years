import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected_years",
    [
        pytest.param(0,
                     0,
                     [0, 0],
                     id="cat and/or dog years is 0"),
        pytest.param(-1,
                     -1,
                     "Please enter integer value for cat and dog years",
                     id="cat and/or dog years is less than 0"),
        pytest.param(14,
                     14,
                     [0, 0],
                     id="first 15 cat or dog years give 1 human year"),
        pytest.param(15,
                     15,
                     [1, 1],
                     id="the next 9 cat or dog years give 1 more human year"),
        pytest.param(28,
                     28,
                     [3, 2],
                     id="every 4 next cat years give 1 extra human year"),
        pytest.param(100,
                     100,
                     [21, 17],
                     id="every 5 next dog years give 1 extra human year"),
        pytest.param(101,
                     101,
                     "Please make sure that you cat or dog"
                     " has more then 100 years",
                     id="cat and/or dog years is more then 100 years")
    ]
)
def test_get_human_age(cat_years: int,
                       dog_years: int,
                       expected_years: list) -> None:
    assert get_human_age(cat_years, dog_years) == expected_years
