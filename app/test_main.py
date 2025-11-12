import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, age_in_human_years",
    [
        (-1, -1, [0, 0]),
        (12, 13, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (0, 0, [0, 0]),
        (100, 100, [21, 17]),
        (0, 150, [0, 27])
    ],
    ids=[
        "not valid negative animal age",
        "animal age less then 15",
        "animal age on the border: 14",
        "animal age on the border: 15",
        "animal age on the border: 23",
        "animal age on the border: 24",
        "animal age on the border: 27",
        "animal age on the border: 28",
        "extremely small animal age",
        "extremely large animal age",
        "cross-referenced animal age"
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       age_in_human_years: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == age_in_human_years


def test_invalid_string_as_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("a", "b")
