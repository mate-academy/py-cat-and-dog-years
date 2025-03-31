import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (14, 14, [0, 0])
    ]
)
def test_should_return_zeros_when_ages_less_15(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result, (
        "Function should return zeros when ages less 15"
    )


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (15, 15, [1, 1])
    ]
)
def test_should_return_ones_when_ages_equal_fithteen(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result, (
        "Function should return ones when ages equal fithteen"
    )


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (23, 23, [1, 1])
    ]
)
def test_should_rounds_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result, (
        "Function should rounds age"
    )


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (25, 25, [2, 2]),
        (26, 26, [2, 2]),
        (27, 25, [2, 2]),
        (26, 27, [2, 2])
    ]
)
def test_should_add_one_year_next_nine_years(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result, (
        "Function should add one year next nine years"
    )


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (28, 28, [3, 2]),
        (32, 28, [4, 2]),
        (38, 28, [5, 2])
    ]
)
def test_should_add_one_year_every_four_cat_years(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result, (
        "Function should add one year every four cat's years"
    )


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (28, 29, [3, 3]),
        (28, 34, [3, 4]),
        (28, 39, [3, 5]),
        (28, 45, [3, 6])
    ]
)
def test_should_add_one_year_every_five_dog_years(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result, (
        "Function should add one year every four cat's years"
    )


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (28, "word"),
        ("True", 29)
    ]
)
def test_should_take_int_arguments(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
