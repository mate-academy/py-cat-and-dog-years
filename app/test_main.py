import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (1, 1, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (30, 30, [3, 3]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_get_human_age_negative_input() -> None:
    assert get_human_age(-1, 16) == [0, 1]


def test_get_human_age_excessive_input() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(101, 100) == [0, 17]


def test_get_human_age_boundary_input() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(27, 28) == [2, 2]


def test_get_human_age_invalid_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", "15")
