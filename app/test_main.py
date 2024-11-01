from typing import Any

import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (-1, -2, [0, 0])
    ]
)
def test_less_than_15_animal_years_should_give_0_human(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), "Animal years less than 15 should give 0 human years"


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (27, 23, [2, 1])
    ]
)
def test_less_than_28_animal_years_should_not_exceed_2_human(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert (get_human_age(cat_age, dog_age) == result), \
        "Animal years less than 28 should give not more as 2 human years"


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_both_more_than_28_animal_years_should_not_be_human_equal(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert (get_human_age(cat_age, dog_age) == result), \
        "Animal years both more than 28 should give different human years"


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("28", "28"),
        (None, 15),
        ([24], [42])
    ]
)
def test_can_not_use_strings(
        cat_age: Any,
        dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
