import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
    ],
)
def test_various_age_cases(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


negative_age_data = [
    (0, -1),
    (-1, 0),
    (-1, -1),
]


@pytest.mark.parametrize("cat_years,dog_years", negative_age_data)
def test_negative_age(cat_years: int, dog_years: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_years, dog_years)


large_age_data = [
    (1_000_000, 1),
    (1, 1_000_000),
    (1_000_000, 1_000_000),
]


@pytest.mark.parametrize("cat_years,dog_years", large_age_data)
def test_very_large_number(cat_years: int, dog_years: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_years, dog_years)


invalid_type_data = [
    ({}, 5),
    ([], 2),
    ("str", -1),
    ([1, 2], -1),
    ({1, 2}, -1),
    ({"a": "1"}, -1),
]


@pytest.mark.parametrize("cat_years,dog_years", invalid_type_data)
def test_age_is_number(cat_years: object, dog_years: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)


next_years_data = [
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (28, 29, [3, 3]),
    (100, 100, [21, 17]),
]


@pytest.mark.parametrize("cat_years,dog_years,expected", next_years_data)
def test_each_next_years_after_24(
    cat_years: int, dog_years: int, expected: list[int]
) -> None:
    assert get_human_age(cat_years, dog_years) == expected
