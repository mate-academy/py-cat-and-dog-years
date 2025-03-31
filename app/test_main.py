import pytest

from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            14,
            14,
            [0, 0],
            id="animal_age_less_than_15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="animal_age_equal_15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="animal_age_less_than_24"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="animal_age_equal_24"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="animal_age_equal_27"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="cat_and_dog_age_equal_28"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="cat_and_dog_age_equal_100"
        ),
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="cat_and_dog_age_less_than_0"
        ),
        pytest.param(
            28,
            15,
            [3, 1],
            id="cat_and_dog_with_diferent_ages"
        )
    ]
)
def test_check_human_age_when_animals_age_are_numbers(
    cat_age: int,
    dog_age: int,
    result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            {},
            "",
            TypeError
        )
    ]
)
def test_check_human_age_when_animals_age_are_not_numbers(
    cat_age: Any,
    dog_age: Any,
    result: TypeError
) -> None:
    with pytest.raises(result):
        get_human_age(cat_age, dog_age)
