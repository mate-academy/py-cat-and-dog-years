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
        (14, 15, [0, 1]),
        (15, 14, [1, 0]),
        (23, 24, [1, 2]),
        (24, 23, [2, 1]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (32, 33, [4, 3]),
        (33, 34, [4, 4]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_with_float() -> None:
    with pytest.raises(TypeError):
        get_human_age(1.5, 2)


def test_get_human_age_with_bool() -> None:
    with pytest.raises(TypeError):
        get_human_age(True, 5)