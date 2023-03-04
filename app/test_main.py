import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (-1, -5, [0, 0]),
        (14, 14, [0, 0]),
        (15, 17, [1, 1]),
        (24, 26, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "return 0 when values < 0",
        "calculate age of cats or dogs who are younger than 15",
        "calculate age of cats or dogs in age between 15 and 23",
        "calculate age of cats or dogs in age between 24 and 27",
        "calculate age of cats or dogs who are elder than 28",
        "calculate big age"
    ]
)
def test_calculate_right_values(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == human_age
    ), (
        f"Human age should be equal to {human_age[0]} if cat age is {cat_age}"
        f"and {human_age[1]} if dog age is {dog_age}"
    )


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("1", "23"),
        ([1, 3], [4, 5]),
        (1, "25")
    ]
)
def test_age_should_be_int(cat_age: int | str, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
