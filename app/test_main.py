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
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (0, 29, [0, 3]),
        (28, 0, [3, 0]),
    ],
)
def test_age_conversion(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("ages", [("15", 15), (15, "15"), (None, 15)])
def test_invalid_age_type(ages: tuple) -> None:
    with pytest.raises(TypeError):
        get_human_age(*ages)
