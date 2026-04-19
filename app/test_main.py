import pytest
import app.main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 15, [0, 1]),
        (24, 23, [2, 1]),
        (28, 28, [3, 2]),
        (100, 1, [21, 0]),
        (15, 24, [1, 2]),
    ],
    ids=[
        "zero_age",
        "cat_0_dog_1",
        "cat_2_dog_1",
        "diff_after_24",
        "extreme_diff",
        "cat_1_dog_2"
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert app.main.get_human_age(cat_age, dog_age) == expected
