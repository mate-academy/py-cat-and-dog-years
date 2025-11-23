import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -5, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (20, 20, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 30, [3, 3]),
        (29, 34, [3, 4]),
        (50, 50, [8, 7]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age_parametrized(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 10),
        (10, "10"),
        (None, 10),
        (10, None),
        ([], {}),
    ]
)
def test_get_human_age_invalid_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
