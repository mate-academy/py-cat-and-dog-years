import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-5, 14, [0, 0]),
        (15, 23, [1, 1]),
        (24, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 30, [3, 3]),
        (1000, 999, [246, 197])
    ],
    ids=[
        "human age should be 0 if cat or dog age is less than 15",
        "human age should be 1 if cat or dog age is over 14 but less than 24",
        "should give 1 more human year if dog or cat years "
        "are equal or more than 24",
        "should give 1 extra human year for every 4 cat years over 24",
        "should give 1 extra human year for every 5 dog years over 24",
        "should work with big numbers"
    ]
)
def test_should_return_correct_results(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == result)


def test_shoud_raise_error() -> None:
    with pytest.raises(TypeError):
        (get_human_age("25", 12))
