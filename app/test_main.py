from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_list",
    [
        pytest.param(
            -10, -3, [0, 0],
            id="should convert 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="should convert first 14 years into 0"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="should convert first 15 years into 1"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="should convert into 1"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="should convert next 9 years into 1 more"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="every next 4 cat years into 1, and same for 5 dog years"
        )
    ]
)
def test_converting_to_human_years(
        cat_age: int,
        dog_age: int,
        expected_list: int
) -> None:
    converted_years = get_human_age(cat_age, dog_age)
    assert converted_years == expected_list


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(
            17, "invalid",
            id="should return error if dog age invalid"
        ),
        pytest.param(
            "invalid", 24,
            id="should return error if cat age invalid"
        )
    ]
)
def test_raising_error_correctly(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
