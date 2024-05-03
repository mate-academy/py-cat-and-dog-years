import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_years",
    [
        (-1, -3, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "Should convert negative into 0",
        "Should convert 14 cat/dog age into 0 human years",
        "Should convert 15 cat/dog age into 1 human years",
        "Should convert 23 cat/dog age into 1 human years",
        "Should convert 23 cat/dog age into 2 human years",
        "Should convert 27/28 cat/dog age into 2 human years",
        "Should convert 28/29 cat/dog age into 3 human years",
        "Should convert 100/100 cat/dog age into 21/17 human years",
    ]
)
def test_should_convert_dog_age_into_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_years: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_years


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("invalid", "12"),
        (13.1, "invalid"),
    ],
    ids=[
        "Should raise error when invalid cat age given",
        "Should raise error when invalid dog age given",
    ]
)
def test_should_raise_type_error(
        cat_age: str | float,
        dog_age: str | float
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
