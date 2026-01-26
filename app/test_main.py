import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-10, -5),
    ],
)
def test_raises_value_error_for_negative_ages(
    cat_age: int,
    dog_age: int,
) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("1", 0),
        (0, "2"),
        ("3", "4"),
    ],
)
def test_raises_type_error_for_string_inputs(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (1.0, 0),
        (0, 2.5),
        (3.14, 4.2),
    ],
)
def test_raises_type_error_for_float_inputs(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
