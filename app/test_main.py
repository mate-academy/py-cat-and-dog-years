from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
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
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_raises_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("5", 10)

    with pytest.raises(TypeError):
        get_human_age(5, "10")

    with pytest.raises(TypeError):
        get_human_age("5", "10")


def test_get_human_age_raises_value_error() -> None:
    try:
        get_human_age(-5, 10)
    except ValueError:
        print("Caught ValueError for negative cat age")

    try:
        get_human_age(5, -10)
    except ValueError:
        print("Caught ValueError for negative dog age")

    try:
        get_human_age(-5, -10)
    except ValueError:
        print("Caught ValueError for both negative ages")

    try:
        get_human_age(1000, 200)
    except ValueError:
        print("Caught ValueError for number being too high")

    try:
        get_human_age(50, 1000)
    except ValueError:
        print("Caught ValueError for number being too high")

    try:
        get_human_age(999, 999)
    except ValueError:
        print("Caught ValueError for number being too high")
