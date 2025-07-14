import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17])
    ],
    ids=[
        "zero ages",
        "ages below first threshold",
        "ages equal to first threshold",
        "ages below second threshold",
        "ages equal to second threshold",
        "ages below third threshold",
        "ages equal to third threshold",
        "ages several times greater than third threshold"
    ]
)
def test_should_convert_cat_dog_age_to_human_age_correctly(
        cat_age: int,
        dog_age: int,
        human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
