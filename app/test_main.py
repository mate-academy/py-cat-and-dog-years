import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (50, 50, [8, 7]),
        (-15, 14.5, [0, 0]),
        (23, 25, [1, 2]),
        (27, 25, [2, 2]),
    ],
    ids=[
        "14 cat/dog years -> 0 human age",
        "15 cat/dog years -> 1 human age",
        "50 cat years -> 8 human, 50 dog years -> 7 human",
        "-15 cat -> 0 human, 14.5 dog -> 0 human",
        "23 cat -> 1 human, 25 dog -> 2 human",
        "27 cat -> 2 human, 25 dog -> 2 human",
    ],
)
def test_check_age_converting(cat_age: int, dog_age: int, result: list
                              ) -> None:
    assert get_human_age(cat_age, dog_age) == result
