import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age", [
        pytest.param(0, 0, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(28, 28, [3, 2]),
        pytest.param(100, 100, [21, 17])
    ],
    ids=[
        "should return zeros when value are zero",
        "should return zero if the value is less than zero human years",
        "first year of life",
        "same age but different for animals",
        "correct age converter in long term"
    ]
)
def test_check_for_cat_age(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
