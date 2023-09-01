from typing import Type

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0, 0, [0, 0],
            id="should check zero age"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="should check age under 1 human year"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="should check animal age right in 1 human year"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="should check animal age above 1 human year"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="should check animal age right in 2 human years"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="should check animal age about 3 human years"
        ),
        pytest.param(
            32, 40, [4, 5],
            id="should check animal age above 2 human years"
        ),
        pytest.param(
            -1, -9, [0, 0],
            id="should check negative ages"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="should check large ages"
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "cat",
            17,
            TypeError,
            id="Age of cat should be an integer"
        ),
        pytest.param(
            25,
            "dog",
            TypeError,
            id="Age of dog should be an integer"
        ),
        pytest.param(
            "cat",
            "dog",
            TypeError,
            id="Age of animals should be an integer"
        ),
        pytest.param(
            "cat",
            None,
            TypeError,
            id="Age of animal can't be None"
        )
    ]
)
def test_get_human_age_with_incorrect_type(
        cat_age: int,
        dog_age: int,
        expected_error: Type[TypeError]) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
