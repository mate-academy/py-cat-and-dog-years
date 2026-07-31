import pytest
import app.main


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
def test_get_human_age_valid_inputs(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert app.main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        ([1, 2], 5),
    ]
)
def test_get_human_age_incorrect_types(cat_age: any, dog_age: any) -> None:
    with pytest.raises(TypeError):
        app.main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (5, -1),
        (-10, -10),
    ]
)
def test_get_human_age_negative_numbers(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        app.main.get_human_age(cat_age, dog_age)
