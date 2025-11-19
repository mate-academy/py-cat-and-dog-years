import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0])
    ],
)
def test_human_age_calculating(
        cat_years: int,
        dog_years: int,
        expected_result: list[int]
) -> None:
    assert get_human_age(cat_years, dog_years) == expected_result, (
        f"Function should return {expected_result}"
        f"when cat_years is equal to {cat_years}"
        f"and dog_years us equal to {dog_years}"
    )


@pytest.mark.parametrize(
    "cat_years, dog_years, expected_error",
    [
        ("3", "t", TypeError),
    ],
)
def test_cat_and_dog_years(
        cat_years: int,
        dog_years: int,
        expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_years, dog_years)
