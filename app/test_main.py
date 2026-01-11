import pytest
from app.main import convert_to_human, get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (1, 1, (0, 0)),
        (14, 14, (0, 0)),
        (15, 15, (1, 1)),
        (23, 24, (2, 2)),
        (28, 29, (3, 3)),
    ]
)
def test_get_human_age(cat_age: float, dog_age: float, expected: tuple[int, int]) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (1, 1, (0, 0)),
        (14, 14, (0, 0)),
        (15, 15, (1, 1)),
        (23, 24, (2, 2)),
        (28, 29, (3, 3)),
    ]
)

def test_get_human_age(cat_age: float, dog_age: float, expected: tuple[int, int]) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected, f"Ожидалось {expected}, получено {result}"
