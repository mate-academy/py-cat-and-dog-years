from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        pytest.param(0, 0,
                     [0, 0],
                     id="Check if human age is 0"),
        pytest.param(14, 14,
                     [0, 0],
                     id="Check if human age is 0 when cat/dog age is 14"),
        pytest.param(15, 15,
                     [1, 1],
                     id="Check if human age is 1 when cat/dog age is 15"),
        pytest.param(23, 23,
                     [1, 1],
                     id="Check if human age is 1 when cat/dog age is 23"),
        pytest.param(24, 24,
                     [2, 2],
                     id="Check if human age is 2 when cat/dog age is 24"),
        pytest.param(27, 27,
                     [2, 2],
                     id="Check if human age is 2 when cat/dog age is 27"),
        pytest.param(28, 28,
                     [3, 2],
                     id="Check if human age is 3/2 when cat/dog age is 28"),
        pytest.param(45, 45,
                     [7, 6],
                     id="Check if human age is 7/6 when cat/dog age is 45")
    ]
)
def test_get_human_age_from_range_ages(
        cat_age: int,
        dog_age: int,
        expected_human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param("five",
                     "ten",
                     id="Ages should be integer, not string type"),
        pytest.param([0],
                     [25],
                     id="Ages should be integer, not list type"),
        pytest.param(0,
                     "0",
                     id="Both ages should be integer"),
    ]
)
def test_get_human_age_with_incorrect_data_types(
        cat_age: Any, dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
