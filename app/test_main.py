import pytest
import app.main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [(0, 0, [0, 0]),
     (14, 14, [0, 0]),
     (15, 15, [1, 1]),
     (23, 23, [1, 1]),
     (24, 24, [2, 2]),
     (27, 27, [2, 2]),
     (28, 28, [3, 2]),
     (29, 29, [3, 3]),
     (100, 100, [21, 17]),
     (1000000, 1000000, [249996, 199997])])
def test_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert app.main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1)])
def test_negative_age_raises_value_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        app.main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 10),
        (15.5, 10),
        (10, "15"),
        (10, 15.5),
        (None, 10),
        (10, None)
    ],
)
def test_invalid_type_raises_type_error(
    cat_age: str | int | float | None,
    dog_age: str | int | float | None,
) -> None:
    with pytest.raises(TypeError):
        app.main.get_human_age(cat_age, dog_age)
