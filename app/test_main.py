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
        (10_000, 10_000, [2496, 1997]),
    ]
)
def test_get_human_age_standard_cases(cat_age, dog_age, expected) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (-10, 0),
        (5, -3),
        (-100, -100),
    ]
)
def test_get_human_age_negative_inputs(cat_age, dog_age) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        ([15], 15),
        (15, {"age": 15}),
    ]
)
def test_get_human_age_invalid_types(cat_age, dog_age) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


def test_all_elements_are_integers() -> None:
    result = get_human_age(100, 100)
    assert all(isinstance(x, int) for x in result)
