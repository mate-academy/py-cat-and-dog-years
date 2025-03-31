import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,cat_age_as_human_age",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
        (100, 21)
    ],
    ids=[
        "range less then 15, age 0 must give 0 human age",
        "range less then 15, age 14 must give 0 human age",
        "first 15 years must give 1 human age",
        (
            "renge more or equal to 15 "
            "and less then age 15 + 9 must give 1 human age"
        ),
        "age 15 + 9 must give 2 human age",
        "age less then 15 + 9 + 4 must give 2 human age",
        "age equal 15 + 9 + 4 must give 3 human age",
        (
            "age more then 15 + 9 + 4 must calculate "
            "each extra 4 years as 1 human age"
        )
    ]
)
def test_check_cat_age_as_human_age(
    cat_age: int,
    cat_age_as_human_age: int
) -> None:
    assert get_human_age(cat_age, 0) == [cat_age_as_human_age, 0]


@pytest.mark.parametrize(
    "dog_age,dog_age_as_human_age",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (29, 3),
        (100, 17)
    ],
    ids=[
        "range less then 15, age 0 must give 0 human age",
        "range less then 15, age 14 must give 0 human age",
        "first 15 years must give 1 human age",
        (
            "renge more or equal to 15 "
            "and less then age 15 + 9 must give 1 human age"
        ),
        "age 15 + 9 must give 2 human age",
        "age less then 15 + 9 + 5 must give 2 human age",
        "age equal 15 + 9 + 5 must give 3 human age",
        (
            "age more then 15 + 9 + 5 must calculate "
            "each extra 5 years as 1 human age"
        )
    ]
)
def test_check_dog_age_as_human_age(
    dog_age: int,
    dog_age_as_human_age: int
) -> None:
    assert get_human_age(0, dog_age) == [0, dog_age_as_human_age]
