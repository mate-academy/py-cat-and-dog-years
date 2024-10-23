import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_year,dog_year,expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2])
    ]
)
def test_should_equal_expected_result(
    cat_year: int,
    dog_year: int,
    expected_result: list[int]
) -> None:
    assert get_human_age(cat_year, dog_year) == expected_result


@pytest.mark.parametrize(
    "cat_year,dog_year",
    [
        (15, 15),
        (23, 23),
        (17, 17)
    ]
)
def test_should_return_one_for_specific_years(
    cat_year: int,
    dog_year: int
) -> None:
    assert get_human_age(cat_year, dog_year) == [1, 1]


@pytest.mark.parametrize(
    "cat_year,dog_year",
    [
        (28, 28),
        (100, 100),
        (24, 24),
        (0, 0)
    ]
)
def test_years_within_valid_range(
    cat_year: int,
    dog_year: int
) -> None:
    human_cat_year, human_dog_year = get_human_age(cat_year, dog_year)
    assert 0 <= human_cat_year <= 100
    assert 0 <= human_dog_year <= 100


@pytest.mark.parametrize(
    "cat_year,dog_year",
    [
        ("17", 15),
        ((7 + 5j), (5 + 8j)),
        (None, 15),
        ([24], [24])
    ],
    ids=[
        "string-and-int",
        "complex-and-complex",
        "none-and-int",
        "list[int]-and-list[int]"
    ]
)
def test_should_raise_correct_exception_if_function_receive_an_incorrect_type(
        cat_year: Any,
        dog_year: Any,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_year, dog_year)
