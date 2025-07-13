import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, result",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "cat and dog have 0 age",
        "cat and dog have 1 human year",
        "cat and dog have 2 human years",
        "cat is 3 human years, dog is 2 human years",
        "cat's and dog's human years are different"
    ]
)
def test_method(cat_years: int, dog_years: int, result: list) -> None:
    assert get_human_age(cat_years, dog_years) == result
