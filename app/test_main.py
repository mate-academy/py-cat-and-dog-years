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
    "cat_years,dog_years",
    [
        (i, j)
        for i in range(0, 15)
        for j in [0, 7, 15, 22, 24, 26, 31]
    ]
)
def test_if_cat_has_zero_years(cat_years: int, dog_years: int) -> None:
    assert (
        get_human_age(cat_years, dog_years)[0] == 0
    ), f"cat age should be 0 if parameter is {cat_years}"


@pytest.mark.parametrize(
    "cat_years,dog_years",
    [
        (i, j)
        for i in [0, 7, 15, 22, 24, 26, 31]
        for j in range(0, 15)
    ]
)
def test_if_dog_has_zero_years(cat_years: int, dog_years: int) -> None:
    assert (
        get_human_age(cat_years, dog_years)[1] == 0
    ), f"dog age should be 0 if parameter is {dog_years}"


@pytest.mark.parametrize(
    "cat_years,dog_years",
    [
        (i, j)
        for i in range(15, 24)
        for j in [0, 7, 15, 22, 24, 26, 31]
    ]
)
def test_if_cat_has_one_years(cat_years: int, dog_years: int) -> None:
    assert (
        get_human_age(cat_years, dog_years)[0] == 1
    ), f"cat age should be 1 if parameter is {cat_years}"


@pytest.mark.parametrize(
    "cat_years,dog_years",
    [
        (i, j)
        for i in [0, 7, 15, 22, 24, 26, 31]
        for j in range(15, 24)
    ]
)
def test_if_dog_has_one_years(cat_years: int, dog_years: int) -> None:
    assert (
        get_human_age(cat_years, dog_years)[1] == 1
    ), f"dog age should be 1 if parameter is {dog_years}"


@pytest.mark.parametrize(
    "cat_years,dog_years",
    [
        (i, j)
        for i in range(24, 100)
        for j in [0, 7, 15, 22, 24, 26, 31]
    ]
)
def test_if_cat_has_two_or_more_years(cat_years: int, dog_years: int) -> None:
    assert (
        get_human_age(cat_years, dog_years)[0] == 2 + (cat_years - 24) // 4
    ), f"cat age should be {2 + (cat_years - 24) // 4}" \
       f" if parameter is {cat_years}"


@pytest.mark.parametrize(
    "cat_years,dog_years",
    [
        (i, j)
        for i in [0, 7, 15, 22, 24, 26, 31]
        for j in range(24, 100)
    ]
)
def test_if_dog_has_two_or_more_years(cat_years: int, dog_years: int) -> None:
    assert (
        get_human_age(cat_years, dog_years)[1] == 2 + (dog_years - 24) // 5
    ), f"dog age should be {2 + (dog_years - 24) // 5}" \
       f" if parameter is {dog_years}"
