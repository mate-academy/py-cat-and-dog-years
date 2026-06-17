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
