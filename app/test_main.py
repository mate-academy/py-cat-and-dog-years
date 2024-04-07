import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (-5, -5, [0, 0]),
        (-100, -100, [0, 0]),
    ],
    ids=[
        "Both zero",
        "Both 14",
        "Both 15",
        "Both 23",
        "Both 24",
        "Both 27",
        "Cat 28, Dog 28",
        "Both 29",
        "Both 100",
        "Both -5",
        "Both -100",
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_human_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


def test_get_human_age_invalid_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")
