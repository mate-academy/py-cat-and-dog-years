import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,value",
    [
        (0, 0, [0, 0]),
        (200, 200, [46, 37]),
        (15, 17, [1, 1]),
        (5, 30, [0, 3]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_should_equal_to_correct_value(
        cat_age: int,
        dog_age: int,
        value: int
) -> None:
    assert get_human_age(cat_age, dog_age) == value


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (26.6, 24.4),
        ("16", "18"),
        (-15, -19),
        (None, None),
        ((43), (73)),
        ([64], [96, 6, 9]),
        ({"k": 3}, {"l": "adf"}),
    ]
)
def test_when_function_takes_non_integer_values(
        cat_age,
        dog_age
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
