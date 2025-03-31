import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (14, 14, [0, 0]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-50, -45, [0, 0]),
        (0, 0, [0, 0])
    ],
    ids=[
        "14 cat/dog years should return 0 human age",
        "28 cat/dog years should return 3/2 human age",
        "100 cat/dog years should return 21/17 human age",
        "returns 0/0 human age with negative cat/dog years",
        "returns 0/0 human age with 0 cat/dog years"
    ]
)
def test_if_function_return_correct_results(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
