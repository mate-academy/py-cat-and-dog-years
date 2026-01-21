import pytest
from app.main import get_human_age


@pytest.mark.parametrize("age, expected",
                         [pytest.param(10, [0, 0],
                                       id="test less one year"),
                          pytest.param(15, [1, 1],
                                       id="test first year"),
                          pytest.param(24, [2, 2],
                                       id="test second ears"),
                          pytest.param(28, [3, 2],
                                       id="test 3 years for cat, "
                                          "and 2 year for dog"),
                          pytest.param(88, [18, 14], id="count years")])
def test_get_human_age(age, expected):
    human_age = get_human_age(age, age)
    assert human_age == expected
