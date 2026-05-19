import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 26, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_cannot_have_negative_ages() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 0)
    with pytest.raises(ValueError):
        get_human_age(0, -1)


def test_can_add_only_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 12)
    with pytest.raises(TypeError):
        get_human_age(15.3, 12)
