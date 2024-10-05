import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_answer",
    [
        pytest.param(0, 0, [0, 0], id="the age should be 0"),
        pytest.param(14, 14, [0, 0],
                     id="the age below 15 should result in 0 output"),
        pytest.param(15, 15, [1, 1],
                     id="the input age of 15 should give 1 year in output"),
        pytest.param(23, 23, [1, 1],
                     id="the age below 24 should result in 1 output"),
        pytest.param(24, 24, [2, 2],
                     id="the age of 24 should give 2 years in output"),
        pytest.param(28, 28, [3, 2],
                     id="the age of 28 should result in "
                        "3 years for cats and 2 years for dog"),
        pytest.param(100, 100, [21, 17],
                     id="the result for 100 years"
                        " should be [21, 17]"),

    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_answer: list) -> None:
    assert expected_answer == get_human_age(cat_age, dog_age)
