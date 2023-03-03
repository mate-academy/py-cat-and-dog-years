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
        "pet age equals 0",
        "pet age is less than 1 human year",
        "pet age equals to 1 human year ",
        "pet age equals to 1 human year ",
        "pet age equals to 2 human years ",
        "pet age equals to 2 human years ",
        "pet age equals to 3 human years",
        "pet age equals to 8 human years",
    ]
)
def test_human_years(cat: int, dog: int, human: list[int]) -> None:
    assert get_human_age(cat, dog) == human


def years_should_not_be_less_than_0() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, -1)
