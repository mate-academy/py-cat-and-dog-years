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
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_function_core_logic_conversion(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-10, -5)
    ]
)
def test_get_human_age_negative_input_raises_value_error(cat_age: int,
                                                         dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (15, "15"),
        ("15", 15),
        (15.5, 15),
        (15, 15.5),
        (True, 15),
        (14, False),
        (15, None),
        (None, 15)
    ]
)
def test_get_human_age_typeerror_input_raises_error(cat_age: int,
                                                    dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
