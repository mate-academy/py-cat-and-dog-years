import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (500, 1001, [121, 197]),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_large_ages() -> None:
    assert get_human_age(500, 1001) == [121, 197]


def test_both_animals_different_ages() -> None:
    assert get_human_age(24, 20) == [2, 1]
    assert get_human_age(28, 29) == [3, 3]
    assert get_human_age(14, 14) == [0, 0]


if __name__ == "__main__":
    pytest.main()
