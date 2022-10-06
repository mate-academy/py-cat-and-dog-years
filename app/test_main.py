import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_and_dog_years,expected_years",
    [
        pytest.param(
            (14, 14),
            [0, 0],
            id="13 cat and dog years equal 0 human year"
        ),
        pytest.param(
            (15, 15),
            [1, 1],
            id="15 cat and dog years equal 1 human year"
        ),
        pytest.param(
            (23, 23),
            [1, 1],
            id="23 cat and dog years equal 1 human year"
        ),
        pytest.param(
            (24, 24),
            [2, 2],
            id="24 cat and dog years equal 2 human years"
        ),
        pytest.param(
            (28, 28),
            [3, 2],
            id="24 cat and dog years equal 3 and 2 human years"
        ),
        pytest.param(
            (29, 29),
            [3, 3],
            id="29 cat and dog years equal 3 human years"
        ),
        pytest.param(
            (100, 100),
            [21, 17],
            id="100 cat and dog years equal 21 and 17 human years"
        )
    ]
)
def test_get_human_age(cat_and_dog_years: tuple, expected_years: list) -> None:
    assert get_human_age(*cat_and_dog_years) == expected_years
