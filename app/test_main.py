import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_cat_human_age, expected_dog_human_age",
    [
        (0, 0, 0, 0),
        (14, 0, 0, 0),
        (15, 0, 1, 0),
        (0, 14, 0, 0),
        (0, 15, 0, 1),
    ]
)
def test_get_human_age_for_various_ages(
        cat_age: int,
        dog_age: int,
        expected_cat_human_age: int,
        expected_dog_human_age: int
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result[0] == expected_cat_human_age
    assert result[1] == expected_dog_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        ("five", 15, TypeError),
        (15, "five", TypeError),
        ("five", "five", TypeError),
        (-1, 15, ValueError),
        (15, -1, ValueError),
        (-1, -1, ValueError),
        (1500, 15, ValueError),
        (15, 1500, ValueError),
    ]
)
def test_get_human_age_with_invalid_types(
        cat_age: int,
        dog_age: int,
        expected_exception: any) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
