import pytest
from app.main import get_human_age


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
    ],
)
def test_get_human_age_valid(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-10, -10),
    ],
)
def test_get_human_age_negative(cat_age: int, dog_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == [
        0 if cat_age < 0 else get_human_age(cat_age, 0)[0],
        0 if dog_age < 0 else get_human_age(0, dog_age)[1],
    ]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
    ],
)
def test_get_human_age_invalid_type(cat_age: object, dog_age: object) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (15.0, 15, [1, 1]),
        (15, 15.0, [1, 1]),
    ],
)
def test_get_human_age_float_allowed(
    cat_age: float | int, dog_age: float | int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
