import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 14, [0, 0]),
        (15, 23, [1, 1]),
        (24, 27, [2, 2]),
        (28, 28, [3, 2]),
        (0, 0, [0, 0]),
        (-28, -28, [0, 0]),
        (100, 100, [21, 17])
    ],
    ids=[
        "return 0 when age lower 15",
        "return 1 when age upper 15 and lower 24",
        "return 2 years for both",
        "return dogs 3rd year",
        "return 0 when 0",
        "return 0 when -int",
        "return many correct years"
    ]
)
def test_should_return_dogs_correct_years(cat_age: int, dog_age: int,
                                          expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_should_raise_error_if_dog_age_is_not_an_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", "23")
