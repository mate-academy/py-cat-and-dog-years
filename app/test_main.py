import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dogs_years, expected",
    [
        pytest.param(0, 0, [0, 0], id="test for zero years"),

        pytest.param(
            14, 14, [0, 0], id="test 14 years before  first_year change"
        ),
        pytest.param(
            15, 15, [1, 1], id="test 15 years after first_year change"
        ),
        pytest.param(
            23, 23, [1, 1], id="test 23 years before to second_year change"
        ),
        pytest.param(
            24, 24, [2, 2], id="test 24 years after second_year change"
        ),

        pytest.param(27, 27, [2, 2], id="test 27 years before third stage"),
        pytest.param(
            28, 28, [3, 2], id="test 28 years difference between cat and dog"
        ),
        pytest.param(
            29, 29, [3, 3], id="test 29 years after third stage for both"
        ),

        pytest.param(28, 28, [3, 2], id="test 28 years difference to cat/dog"),
        pytest.param(32, 32, [4, 3], id="test 32 years difference to cat/dog"),
        pytest.param(33, 33, [4, 3], id="test 33 years difference to cat/dog"),

        pytest.param(36, 36, [5, 4], id="test 36 years difference to cat/dog"),
        pytest.param(40, 40, [6, 5], id="test 40 years difference to cat/dog"),

        pytest.param(100, 100, [21, 17], id="test for long livers"),
    ],
)
def test_get_human_age(
        cat_years: int, dogs_years: int, expected: list
) -> None:
    assert get_human_age(cat_years, dogs_years) == expected
