import pytest

from .main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected_output",
    [
        pytest.param(0, 0, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(28, 28, [3, 2]),
        pytest.param(100, 100, [21, 17])
    ],
    ids=["should return only two values",
         "should return correct years for young animals",
         "should return more years to cat when mature and equal",
         "should return correct years for matured animals",
         "should return correct years for old animals"
         ]
)
def test_correct_human_age_conversion(
        cat_years: int,
        dog_years: int,
        expected_output: list
) -> None:
    assert get_human_age(cat_years, dog_years) == expected_output
