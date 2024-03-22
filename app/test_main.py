import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (
            0, 0, [0, 0]
        ),
        (
            15, 15, [1, 1]
        ),
        (
            24, 24, [2, 2]
        ),
        (
            29, 28, [3, 2]
        ),
    ]
)
def test_can_count_years(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result
