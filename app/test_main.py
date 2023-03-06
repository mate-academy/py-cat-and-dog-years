import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "pet age equals 0",
        "pet age is less than 1 human year",
        "pet age equals to 1 human year ",
        "pet age is less than 2 human year ",
        "pet age equals to 2 human years ",
        "pet age is less than 3 human years ",
        "cat age equals to 3 human years",
        "pet age equals 100 years",
    ]
)
def test_can_sum(cat_age: int, dog_age: int, human_age: list) -> None:
    assert (get_human_age(cat_age, dog_age) == human_age)
