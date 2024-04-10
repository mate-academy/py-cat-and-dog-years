import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
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
        (-5, -5, [0, 0]),
        (-100, -100, [0, 0]),
    ],
    ids=[
        "Dog and Cat ages 0 must equal 0 human ages",
        "Dog and Cat ages 14 must equal 0 human ages",
        "Dog and Cat ages 15 must equal 1 human ages",
        "Dog and Cat ages 23 must equal 1 human ages",
        "Dog and Cat ages 22 must equal 2 human ages",
        "Dog and Cat ages 27 must equal 2 human ages",
        "Dog and Cat ages 28 must equal 3 human ages "
        "for Cat and 2 human ages for Dog",
        "Dog and Cat ages 29 must equal 3 human ages",
        "Dog and Cat ages 100 must equal 21 human ages "
        "for Cat and 17 human ages for Dog",
        "Dog and Cat ages -5 must equal 0 human ages",
        "Dog and Cat ages -100 must equal 0 human ages",
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


@pytest.mark.parametrize(
    "invalid_input",
    [
        ("cat", "dog"),
        (None, None),
        ({}, []),
    ]
)
def test_get_human_age_invalid_input(invalid_input: tuple) -> None:
    with pytest.raises(TypeError):
        get_human_age(*invalid_input)
