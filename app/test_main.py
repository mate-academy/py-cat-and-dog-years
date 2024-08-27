from typing import Any
import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age_list",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="0 cat/dog years should convert into 0 human age."),
        pytest.param(
            14,
            14,
            [0, 0],
            id="14 cat/dog years should convert into 0 human age."),
        pytest.param(
            15,
            15,
            [1, 1],
            id="15 cat/dog years should convert into 1 human age."),
        pytest.param(
            23,
            23,
            [1, 1],
            id="23 cat/dog years should convert into 1 human age."),
        pytest.param(
            24,
            24,
            [2, 2],
            id="24 cat/dog years should convert into 2 human age."),
        pytest.param(
            27,
            28,
            [2, 2],
            id="27/28 cat/dog years should convert into 2 human age."),
        pytest.param(
            28,
            29,
            [3, 3],
            id="28/29 cat/dog years should convert into 3 human age."),
        pytest.param(
            100,
            100,
            [21, 17],
            id="cat/dog years should convert considering each_year."),
        pytest.param(
            -2,
            4,
            [0, 0],
            id="negative cat years should convert into 0 human age."),
        pytest.param(
            15,
            -12,
            [1, 0],
            id="negative dog years should convert into 0 human age."),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_age_list: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age_list


def test_large_ages() -> None:
    assert get_human_age(1000, 1000) == [246, 197]


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param("11", 10, TypeError),
        pytest.param(10, "26", TypeError),
        pytest.param("10", "26", TypeError),
    ]
)
def test_invalid_types(
        cat_age: int,
        dog_age: int,
        expected_error: Any,
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
