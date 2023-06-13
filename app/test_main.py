import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, result",
    [
        (0, 0, [0, 0]),
        (5, 5, [0, 0]),
        (14, 14, [0, 0]),
        (-1, -1, [0, 0])
    ]
)
def test_should_return_zeros_if_values_less_than_15(
        cat_years: int,
        dog_years: int,
        result: list
) -> None:
    assert get_human_age(cat_years, dog_years) == result


@pytest.mark.parametrize(
    "cat_years, dog_years, result",
    [
        (15, 15, [1, 1]),
        (17, 17, [1, 1]),
        (23, 23, [1, 1])
    ]
)
def test_should_return_ones_if_values_between_15_and_23(
        cat_years: int,
        dog_years: int,
        result: list
) -> None:
    assert get_human_age(cat_years, dog_years) == result


@pytest.mark.parametrize(
    "cat_years, dog_years, result",
    [
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 27, [2, 2])
    ]
)
def test_should_return_deuces_if_values_between_24_and_27(
        cat_years: int,
        dog_years: int,
        result: list
) -> None:
    assert get_human_age(cat_years, dog_years) == result


@pytest.mark.parametrize(
    "cat_years, dog_years, result",
    [
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_should_return_different_results_if_values_more_than_27(
        cat_years: int,
        dog_years: int,
        result: list
) -> None:
    assert get_human_age(cat_years, dog_years) == result


@pytest.mark.parametrize(
    "cat_years, dog_years",
    [
        ("28", "28"),
        ([100], [100]),
        ({25}, {25}),
        ((1, 2), (1, 2))
    ]
)
def test_should_raise_error_if_values_not_int(cat_years: int,
                                              dog_years: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)
