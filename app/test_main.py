import pytest


from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (24, 24, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (23, 23, [1, 1]),
    (27, 27, [2, 2]),
    (31, 33, [3, 3]),
    (32, 34, [4, 4]),
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_raises_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("five", 3)

    with pytest.raises(TypeError):
        get_human_age(4, 2.5)


def test_get_human_age_raises_value_error() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 5)

    with pytest.raises(ValueError):
        get_human_age(5, -10)
