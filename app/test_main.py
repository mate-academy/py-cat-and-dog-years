import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years",
    [
        (i, j)
        for i in [0, 7, 15, 22, 24, 26, 31]
        for j in [0, 7, 15, 22, 24, 26, 31]
    ]
)
def test_if_result_has_right_format(cat_years: int, dog_years: int) -> None:
    result = get_human_age(cat_years, dog_years)
    assert (
        isinstance(result, list)
    ), "result should be list"
    assert (
        len(result) == 2
    ), "result list should have 2 items"
    assert (
        isinstance(result[0], int) and isinstance(result[1], int)
    ), "items of result should be int"


@pytest.mark.parametrize(
    "cat_years,dog_years,expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_if_cat_has_years(
        cat_years: int,
        dog_years: int,
        expected_result: list
) -> None:
    assert (
        get_human_age(cat_years, dog_years) == expected_result
    ), f"cat, dog age should be {expected_result[0]}, {expected_result[1]} " \
       f"if parameter is {cat_years}, {dog_years}"
