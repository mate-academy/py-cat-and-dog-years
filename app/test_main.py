import pytest
from app import main


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
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, 0, [0, 0]),
        (0, -1, [0, 0]),
        (10 ** 6, 10 ** 6, [249996, 199997]),
    ]
)
def test_get_human_age_out_of_range(
        cat_age: int, dog_age: int, expected: list) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "age_below, age_at, expected_below, expected_at",
    [
        (14, 15, [0, 0], [1, 1]),
        (23, 24, [1, 1], [2, 2]),
        (27, 28, [2, 2], [3, 2]),
        (28, 29, [3, 2], [3, 3]),
    ]
)
def test_get_human_age_boundaries(
        age_below: int,
        age_at: int,
        expected_below: list,
        expected_at: list,
) -> None:
    assert main.get_human_age(age_below, age_below) == expected_below
    assert main.get_human_age(age_at, age_at) == expected_at


@pytest.mark.parametrize("cat_age, dog_age", [
    ("5", 10),
    (5, "10"),
    (None, 10),
    (10, None),
])
def test_get_human_age_raises_type_error(
        cat_age: object, dog_age: object) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
