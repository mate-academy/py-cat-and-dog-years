import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_boundary_values() -> None:
    assert get_human_age(14, 15) == [0, 1]
    assert get_human_age(15, 14) == [1, 0]
    assert get_human_age(23, 24) == [1, 2]
    assert get_human_age(24, 23) == [2, 1]


def test_large_values() -> None:
    assert get_human_age(200, 200) == [46, 37]
    assert get_human_age(1000, 1000) == [246, 197]
