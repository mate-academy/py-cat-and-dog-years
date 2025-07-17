import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 15, [0, 1]),
        (15, 14, [1, 0]),
        (23, 23, [1, 1]),
        (24, 23, [2, 1]),
        (27, 27, [2, 2]),
    ]
)
def test_get_human_age_changes_only_on_threshold(
        cat_age: int, dog_age: int, expected: list) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (10, -3),
        (-10, -10),
    ]
)
def test_get_human_age_should_raise_for_negative_numbers(
        cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (None, 15),
        (15, "15"),
        (15, {"dog": 15}),
        ([1, 2], 3),
    ]
)
def test_get_human_age_should_raise_for_invalid_types(
        cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
