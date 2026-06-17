import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197])
    ]
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age", [
        ("abc", 12),
        (12, "csd"),
        ("d", "k"),
        (20, 20.5),
        (20.5, 20)

    ]
)
def test_invalid_type(cat_age : int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age", [
        (-10, 20),
        (5, -15),
        (-30, -30)
    ]
)
def test_negative_age(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
