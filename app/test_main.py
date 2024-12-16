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
    ]
)
def test_get_human_age_valid(
        cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_negative() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 10)
    with pytest.raises(ValueError):
        get_human_age(10, -5)


def test_get_human_age_large_values() -> None:
    assert get_human_age(10**6, 10**6) == [249996, 199997]


@pytest.mark.parametrize(
    "cat_age, dog_age", [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
        ([15], 15),
        (15, {"age": 15}),
    ]
)
def test_get_human_age_invalid_types(cat_age: object, dog_age: object) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
