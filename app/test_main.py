from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age,dog_age,expected", [
    (0, 0, [0, 0]),
    (1, 1, [0, 0]),
    (2, 2, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (0, 5, [0, 0]),  # приклад асиметричного
    (5, 0, [0, 0]),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result == expected


def test_get_human_age_negative_raises() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 5)
    with pytest.raises(ValueError):
        get_human_age(5, -2)
    with pytest.raises(ValueError):
        get_human_age(-3, -4)


def test_get_human_age_invalid_type_raises() -> None:
    with pytest.raises(TypeError):
        get_human_age("a", "b")
    with pytest.raises(TypeError):
        get_human_age("5", 3)
    with pytest.raises(TypeError):
        get_human_age(3, 4.5)
