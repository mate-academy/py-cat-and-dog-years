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
        (29, 29, [3, 3]),
        (30, 30, [3, 3]),
        (31, 33, [3, 3]),
        (100, 100, [21, 17]),
        (15, 24, [2, 1]),
        (24, 15, [1, 2]),
        (1000, 1000, [246, 197]),
        (-1, -1, [0, 0]),
        (-100, -100, [0, 0]),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_get_value_error_for_string() -> None:
    with pytest.raises(ValueError):
        get_human_age("100", 100)


def test_get_human_age_get_value_error_for_float() -> None:
    with pytest.raises(ValueError):
        get_human_age(1.1, 1.1)
