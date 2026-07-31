import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_cat, expected_dog",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 27, 2, 2),
        (28, 28, 3, 2),
        (100, 100, 21, 17),
    ]
)
def test_should_return_correct_human_age(
        cat_age: int,
        dog_age: int,
        expected_cat: int,
        expected_dog: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [expected_cat, expected_dog]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-5, -5),
    ]
)
def test_should_return_zero_for_negative_age(
        cat_age: int,
        dog_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, None),
        (None, 15),
        (15, None),
    ]
)
def test_should_raise_type_error_for_invalid_input(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
