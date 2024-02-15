import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (32, 32, [4, 3]),
        (34, 34, [4, 4]),
        (100, 100, [21, 17]),
        (0, 0, [0, 0]),
        (-15, -15, [0, 0]),
        (-1000000, -1000000, [0, 0]),
        (1000000, 1000000, [249996, 199997]),
        (100.4578, 100.4578, [21.0, 17.0]),
    ],
    ids=[
        "0, 0 human age",
        "1, 1 human age",
        "2, 2 human age",
        "3, 2 human age",
        "3, 3 human age",
        "4, 3 human age",
        "4, 4 human age",
        "21, 17 human age",
        "Zero age",
        "Negative age",
        "Large negative age",
        "Large positive age",
        "Float age",
    ]
)
def test_output_should_change_with_some_integer_value(
        cat_age: int,
        dog_age: int,
        human_age: int
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == human_age
    ), f"Convert {cat_age} and {dog_age} should be equal to {human_age}"


@pytest.mark.parametrize(
    "age",
    [
        ([3]),
        ("3"),
        ({3}),
    ],
)
def test_raises_the_correct_exception(age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(age, age)
