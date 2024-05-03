import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_years",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
    ],
    ids=[
        "Should convert 14 cat/dog age into 0 human years",
        "Should convert 15 cat/dog age into 1 human years",
        "Should convert 23 cat/dog age into 1 human years",
        "Should convert 23 cat/dog age into 2 human years",
        "Should convert 27/28 cat/dog age into 2 human years",
        "Should convert 28/29 cat/dog age into 3 human years",
    ]
)
def test_should_convert_dog_age_into_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_years: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_years


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        ("10", "12", TypeError),
        (13.1, 12.333, TypeError),
        (0, 0, ValueError),
        (-2, -1, ValueError),
        (150, 200, ValueError)
    ],
    ids=[
        "Should raise error when string given",
        "Should raise error when float given",
        "Should raise error when zero given",
        "Should raise error when negative given",
        "Should raise error when a large number given",
    ]
)
def test_should_raise_value_error(
        cat_age: str | float,
        dog_age: str | float,
        error: type[Exception]
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
