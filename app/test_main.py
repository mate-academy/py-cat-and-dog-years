import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age,dog_age,result_in_year",
                         [
                             pytest.param(14, 14, [0, 0],
                                          id="14 cat/dog years are 0 human"),
                             pytest.param(15, 15, [1, 1],
                                          id="15 cat/dog years are 1 human"),
                             pytest.param(23, 23, [1, 1],
                                          id="23 cat/dog years are 1 human"),
                             pytest.param(24, 24, [2, 2],
                                          id="24 cat/dog years are 2 human"),
                             pytest.param(28, 29, [3, 3],
                                          id="28 cat 29 dog years are 3 human")
                         ]
                         )
def test_correctness_of_values_get_human_age(cat_age, dog_age,
                                             result_in_year):
    assert get_human_age(cat_age, dog_age) == result_in_year
