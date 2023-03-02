import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,human",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (50, 55, [8, 8])
    ],
    ids=[
        "animal years equal 0",
        "animal years that less than 1 human year",
        "animal years that equal to 1 human year",
        "animal years that equal to 1 human year",
        "animal years that equal to 2 human years",
        "animal years that equal to 2 human years",
        "animal years that equal to 3 human years",
        "animal years that equal to 8 human years",
    ]
)
def test_human_years(cat: int, dog: int, human: list[int]) -> None:
    assert get_human_age(cat, dog) == human


def years_should_be_not_less_than_0() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, -1)
