import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197]),
    ],
)
def test_should_convert_cat_and_dog_ages_to_human_years(
    cat_age: int,
    dog_age: int,
    expected: list,
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
    ],
)
def test_should_raise_type_error_when_age_has_incorrect_type(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
