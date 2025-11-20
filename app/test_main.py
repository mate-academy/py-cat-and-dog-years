import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (0, 500000, [0, 99997]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_conversion_age(cat_age: int, dog_age: int, result: list) -> None:
    assert (get_human_age(cat_age, dog_age) == result)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("0", 0),
        ("abfg", "14"),
        (15, "15.56"),
        (5.54, 14),
        (15, 0.1),
        ([0], {56})

    ]
)
def test_if_wrong_type(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-5, 14, [0, 0]),
        (15, -1, [1, 0]),
        (-10, -56, [0, 0])

    ]
)
def test_if_number_is_negative(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == result)
