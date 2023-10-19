import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected_results",
    [
        (15, 15, [1, 1]),
        (1, 4, [0, 0]),
        (17, 19, [1, 1]),
        (24, 24, [2, 2]),
        (26, 25, [2, 2]),
        (28, 29, [3, 3]),
        (30, 33, [3, 3]),
        (100, 100, [21, 17])
    ],
    ids=[
        "Exactly 1 human year",
        "Less than 1 human year",
        "Less than 2 human years",
        "Exactly 2 human years",
        "Less than 3 human years",
        "Exactly 3 human years",
        "Less than 4 human years",
        "Large animal age numbers",
    ]
)
def test_amimal_years(cat_years: int,
                      dog_years: int,
                      expected_results: list) -> None:
    assert get_human_age(cat_years, dog_years) == expected_results
