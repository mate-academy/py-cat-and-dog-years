import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return zeroes if cat_age and dog_age are zeroes"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should return right values"
        ),
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="should return zeroes if (cat_age and dog age) < 0 "
        ),
        pytest.param(
            1000,
            1000,
            [246, 197],
            id="should work correctly if cat and dog age are large numbers"
        ),
        pytest.param(
            0,
            17,
            [0, 1],
            id="should work correctly if cat age is zero"
        ),
        pytest.param(
            17,
            0,
            [1, 0],
            id="should work correctly if dog age is zero"
        ),
        pytest.param(
            -10000,
            -10000,
            [0, 0],
            id="should return zeroes if values are large numbers and < 0 "
        ),
    ]
)
def test_cat_and_dogs_years_works_correctly(
        cat_age: int,
        dog_age: int,
        expected_human_age: list
) -> None:
    human_age = get_human_age(cat_age, dog_age)
    assert expected_human_age == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(
            1,
            "1",
            id="shoud raise error if one value is str"
        ),
        pytest.param(
            [1, 2],
            2,
            id="should raise error if one value is list"
        ),
        pytest.param(
            (1,),
            2,
            id="should raise error if one value is tuple"
        ),
        pytest.param(
            65,
            {1, 2},
            id="should raise error if one value is set"
        )
    ]
)
def test_check_raises_error_with_list_value(
        cat_age: Any,
        dog_age: Any,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
