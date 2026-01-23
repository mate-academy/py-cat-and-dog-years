import pytest
from app import main


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
        (15, 28, [1, 2]),
        (32, 15, [4, 1]),
    ]
)
def test_get_human_age_logic(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


def test_get_human_age_returns_list() -> None:
    result = main.get_human_age(24, 24)
    assert isinstance(result, list), "Результат має бути списком"
    assert len(result) == 2, "Список має містити рівно два елементи"
