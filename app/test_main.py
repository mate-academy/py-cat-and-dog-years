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
        (-5, -5, [0, 0]),  # Negative numbers edge case
    ],
)
def test_human_parametrize(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "invalid_age",
    [
        "15",
        None,
        [15],
    ],
)
def test_get_human_age_invalid(invalid_age: str | None | list[int]) -> None:
    with pytest.raises(TypeError):
        get_human_age(invalid_age, 15)
    with pytest.raises(TypeError):
        get_human_age(15, invalid_age)
